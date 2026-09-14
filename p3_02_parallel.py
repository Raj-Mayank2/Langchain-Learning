import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-safeguard-20b", temperature=0.7)

parser=StrOutputParser()

pros_prompt=ChatPromptTemplate.from_template("List 3 pros of {topic}. Be concise")
cons_prompt=ChatPromptTemplate.from_template("List 3 cons of {topic}.Be concise")
use_prompt=ChatPromptTemplate.from_template("Give 3 rreal-world use of {topic}.Be concise")

parallel = RunnableParallel(
    pros=pros_prompt | llm | parser,
    cons=cons_prompt | llm | parser,
    uses=use_prompt | llm | parser,
)


result= parallel.invoke({"topic":"electric vechicles"})

print("PROS:\n",result["pros"])
print("\nCONCS:\n",result["cons"])
print("\nUSES:\n",result["uses"])
