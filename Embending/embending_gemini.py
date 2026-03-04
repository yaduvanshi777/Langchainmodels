from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')

result = model.embed_query('give me a great and healthy diet plan')

print(str(result))  