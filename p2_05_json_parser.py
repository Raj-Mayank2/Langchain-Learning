import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()
llm=ChatGroq(model="openai/gpt-oss-safeguard-20b",temperature=0)

prompt=ChatPromptTemplate.from_template(
    "Give me info about the country {country}"
    "Return only valid JSON with keys: name, capital,population,languages(list)."
    "No markdown, no commentary"
)

chain=prompt | llm | JsonOutputParser()

data=chain.invoke({"country":"Japan"})
print(type(data))
print(data)
print("Cpaital:",data["capital"])