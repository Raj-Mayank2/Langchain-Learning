import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-safeguard-20b", temperature=0.9)

prompt = "Write a 100-word short story about a robot learning to paint."

print("📖 Story:\n")
for chunk in llm.stream(prompt):
    print(chunk.content, end="", flush=True)
print()
