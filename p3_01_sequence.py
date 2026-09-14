#Method	Purpose
#.invoke(input)	Single call → one output
#.batch([inputs])	Many calls in parallel
#.stream(input)	Yield chunks as they arrive
#.ainvoke/.abatch/.astream	Async versions
#.with_retry()	Auto-retry on failure
#.with_fallbacks([...])	Fallback to another runnable
#Why this matters: Anything you build with | automatically gets .batch(), .stream(), retries, and fallbacks for free. That's the superpower.


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm=ChatGroq(model="openai/gpt-oss-safeguard-20b",temperature=0.7)

story_prompt=ChatPromptTemplate.from_template("Write a 3-sentence about {topic}")

summary_prompt=ChatPromptTemplate.from_template(
    "Summarize this story in one sentence:\n\n{story}"
)

parser=StrOutputParser()

story_chain=story_prompt | llm | parser
summary_chain= summary_prompt | llm | parser

full_chain=story_chain | (lambda story: {"story":story}) | summary_chain

result=full_chain.invoke({"topic":"a robot learning to paint"})
print (result)