import streamlit as st
from agent import graph
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="TravelBuddy", page_icon="✈️")

st.title("✈️ TravelBuddy - Trợ lý du lịch")

# Khởi tạo session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lịch sử chat
for msg in st.session_state.messages:
    if msg[0] == "human":
        with st.chat_message("user"):
            st.write(msg[1])
    else:
        with st.chat_message("assistant"):
            st.write(msg[1])

# Input người dùng
user_input = st.chat_input("Bạn muốn đi đâu?")

if user_input:
    # Hiển thị user message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append(("human", user_input))

    # Gọi agent
    with st.chat_message("assistant"):
        with st.spinner("TravelBuddy đang suy nghĩ..."):
            result = graph.invoke({"messages": st.session_state.messages})
            st.session_state.messages = result["messages"]

            final = st.session_state.messages[-1]

            st.write(final.content)