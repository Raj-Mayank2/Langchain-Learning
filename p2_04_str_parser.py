import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
llm=ChatGroq(model="openai/gpt-oss-safeguard-20b")

prompt=ChatPromptTemplate.from_template("Tell me a joke about {topic}")
parser=StrOutputParser()

chain= prompt | llm | parser

result=chain.invoke({"topic":"programmers"})
print(type(result))
print(result)