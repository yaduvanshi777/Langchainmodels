from langchain_ollama import ChatOllama
#from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# llm = HuggingFacePipeline.from_model_id(
#     model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task='text-generation',
#     pipeline_kwargs=dict(
#         temperature=0.5,
#         max_new_tokens=100
#     )
# )
# model = ChatHuggingFace(llm=llm)

# result = model.invoke("What is the capital of India")

# print(result.content)

# Connects to your local Ollama server at http://localhost:11434
model = ChatOllama(model="qwen3.5:latest")


result = model.invoke("What is the capital of India")

print(result.content)