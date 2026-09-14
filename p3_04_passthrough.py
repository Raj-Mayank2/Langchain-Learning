import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel

load_dotenv()
llm = ChatGroq(model="openai/gpt-oss-safeguard-20b")
parser = StrOutputParser()

answer_prompt = ChatPromptTemplate.from_template("Answer briefly: {question}")
answer_chain = answer_prompt | llm | parser

# Return BOTH the original question AND the answer
chain = RunnableParallel(
    question=RunnablePassthrough(),   # keeps input as-is
    answer=answer_chain,
)

result = chain.invoke("What is the capital of Australia?")
print(result)
# {'question': 'What is the capital of Australia?', 'answer': 'Canberra.'}