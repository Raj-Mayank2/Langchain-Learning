import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-safeguard-20b",temperature=0.8)

system=SystemMessage(content=(
    "You are a sarcastic Math tutor.You always answer correctly but with witty sarcasm.Keep answer short in 2-3 sentences."

))
questions = [
    "What is 15 * 7?",
    "Solve for x: 2x + 5 = 17",
    "What is the derivative of x^3?",
]

for q in questions:
    print(f"\n Studentl: {q}")
    response=llm.invoke([system,HumanMessage(content=q)])
    print(f"Tutor:{response.content}")



