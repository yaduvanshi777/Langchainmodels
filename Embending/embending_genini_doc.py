from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')

embed_documents = [
    'give me a great and healthy diet plan',
    'give me a  plan for holiday trip'
]

result = model.embed_documents(embed_documents)

print(str(result))  