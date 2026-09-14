import os, time
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-safeguard-20b")

print("---- INVOKE ----")

r=llm.invoke("Name 3 programming languages.")
print(r.content)


print("\n ---- STREAM ----")
for chunk in llm.stream("Write a haiku about coding."):
    print(chunk.content, end="", flush=True)


print("\n\n ---- BATCH ----")
results=llm.batch(["What is 2+4?","What is the capital of JAPAN?"])
for r in results:
    print("->",r.content)