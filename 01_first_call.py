import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API key from .env
load_dotenv()

# Create the LLM object
llm = ChatGroq(
    model="allam-2-7b",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY"),
)

# Send a prompt
response = llm.invoke("Explain LangChain in 2 sentences.")

print(type(response))
print(response.response_metadata)
print(response.content)
print(response.usage_metadata)