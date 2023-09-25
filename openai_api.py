import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# ... rest of the code ...
