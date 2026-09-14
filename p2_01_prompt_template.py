import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm=ChatGroq(model="allam-2-7b")


prompt=PromptTemplate.from_template(
    "Explain {topic} to a {audience} in exactly {n} sentences."
)


filled=prompt.format(topic="quantum computing", audience="10-year-old", n=3)
print("---Filled prompt---")
print(filled)

print("/n --- LLM Response---")
print(llm.invoke(filled).content)