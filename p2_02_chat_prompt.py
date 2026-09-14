import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm = ChatGroq(model="openai/gpt-oss-safeguard-20b")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {persona}. Answer concisely."),
    ("human", "{question}"),
])

messages = prompt.format_messages(persona="pirate chef", question="How do I boil pasta?")
for m in messages:
    print(type(m).__name__, "→", m.content)

print("\n--- Response ---")
print(llm.invoke(messages).content)