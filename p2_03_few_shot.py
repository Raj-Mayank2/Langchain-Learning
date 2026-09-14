import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import FewShotChatMessagePromptTemplate, ChatPromptTemplate

load_dotenv()
llm = ChatGroq(model="openai/gpt-oss-safeguard-20b", temperature=0)

examples = [
    {"input": "happy",  "output": "😄"},
    {"input": "sad",    "output": "😢"},
    {"input": "angry",  "output": "😡"},
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])

few_shot = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

final_prompt = ChatPromptTemplate.from_messages([
    ("system", "Convert the emotion word into a single emoji. Output ONLY the emoji."),
    few_shot,
    ("human", "{input}"),
])

chain_input = final_prompt.format_messages(input="confused")
print(llm.invoke(chain_input).content)   # → 😕

