from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
import os


# Load environment variables
load_dotenv()

# Constants
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Initialize the OpenAI language model
llm = ChatOpenAI(model="gpt-4")
