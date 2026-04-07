import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

#nap bien moi truong
load_dotenv()

#lay token tu github
github_token = os.getenv("GITHUB_TOKEN_4o_mini")

if not github_token:
    raise ValueError("Lỗi: Chưa có GITHUB_TOKEN trong file .env")

#khoi tao model langchain tra ve server cua github
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=github_token, 
    base_url="https://models.inference.ai.azure.com"
)

#test model
print(llm.invoke("Xin chào, bạn là ai?").content)