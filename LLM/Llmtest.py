from google import genai

from dotenv import load_dotenv
import os

load_dotenv()

# Create client with API key
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

# Generate content using gemini-2.5-flash
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="What is the mahindra car n suv mode"
)
print(response.text)

