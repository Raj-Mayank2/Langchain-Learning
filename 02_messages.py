from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm=ChatGroq(model="allam-2-7b")


messages=[
    SystemMessage(content="You are a pirate.Answer everything in pirate speak."),
    HumanMessage(content="What is Python?"),
]

response=llm.invoke(messages)

print(response.content)