
import os
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from tools import search_flights, search_hotels, calculate_budget
from dotenv import load_dotenv

load_dotenv()

# 1. Doc system prompt
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()
    
# 2. Khai bao state
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    
# 3. khoi tao LLM va Tools
tools_list = [search_flights, search_hotels, calculate_budget]
github_token = os.getenv("GITHUB_TOKEN_4o_mini")
if not github_token:
    raise ValueError("Error: chua co token")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=github_token,
    base_url="https://models.inference.ai.azure.com"
)
llm_with_tools = llm.bind_tools(tools_list)

#4. Agent node
def agent_node(state: AgentState):
    messages =  state["messages"]
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] +messages
    
    response = llm_with_tools.invoke(messages)
    
    # LOGGING
    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"Gọi tool: {tc['name']}({tc['args']})")
    else:
        print(f"Trả lời trực tiếp")
    return {"messages": [response]}

# 5. Xây dựng Graph
builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)

tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

# Khai báo edges
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

# Biên dịch đồ thị
graph = builder.compile()

#6. Chat loop
if __name__ == "__main__":
    print("=" * 60)
    print("TravelBuddy - Trợ lý Du lịch Thông minh")
    print("Gõ 'quit' hoặc 'exit' để thoát")
    print("=" * 60)

    # Lịch sử hội thoại
    chat_history = []

    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Tạm biệt! Hẹn gặp lại!")
            break

        print("\nTravelBuddy đang suy nghĩ...")
        
        chat_history.append(("human", user_input))
        # from langchain_core.messages import HumanMessage
        # chat_history.append(HumanMessage(content=user_input))
        
        result = graph.invoke({"messages": chat_history})
        
        # Cập nhật lịch sử và in kết quả
        chat_history = result["messages"]
        final = chat_history[-1]
        
        print(f"\nTravelBuddy: {final.content}")
    
