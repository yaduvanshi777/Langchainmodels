from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

# Llama models tend to ignore subtle format hints and generate code/prose instead.
# A very explicit, strict prompt forces it to output raw JSON only.
template = PromptTemplate(
    template=(
        'You are a JSON generator. Your ONLY job is to output a single valid JSON object. '
        'Do NOT write any explanation, code, markdown, or extra text. '
        'Output ONLY the JSON object and nothing else.\n\n'
        'Generate the name, age and city of a fictional {place} person.\n\n'
        '{format_instruction}'
    ),
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

final_result = chain.invoke({'place': 'sri lankan'})

print(final_result)