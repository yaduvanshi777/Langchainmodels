from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=hf_token,
    max_new_tokens=500,
    task="text-generation",
    
)

model = ChatHuggingFace(llm=llm)

result = model.invoke([HumanMessage(content='give me a great and healthy diet plan')])

print(result.content)