import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

load_dotenv()
llm = ChatGroq(model="openai/gpt-oss-safeguard-20b", temperature=0)

# 1. Define the schema
class Movie(BaseModel):
    title: str = Field(description="Movie title")
    year: int = Field(description="Release year")
    genre: str = Field(description="Primary genre")
    rating: float = Field(description="Rating out of 10")
    cast: List[str] = Field(description="Top 3 cast members")

# 2. Create the parser
parser = PydanticOutputParser(pydantic_object=Movie)

# 3. Build the prompt — parser gives us format instructions
prompt = ChatPromptTemplate.from_template(
    "Give me info about the movie {movie}.\n\n{format_instructions}"
).partial(format_instructions=parser.get_format_instructions())

# 4. Chain
chain = prompt | llm | parser

movie = chain.invoke({"movie": "Inception"})
print(type(movie))          # <class '__main__.Movie'>
print(movie.title)          # Inception
print(movie.year)           # 2010
print(movie.cast)           # ['Leonardo DiCaprio', ...]
print(movie.model_dump())   # dict version