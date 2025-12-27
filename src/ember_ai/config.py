# src/ember_ai/config.py
from dotenv import load_dotenv
import os

load_dotenv()  # <-- THIS LINE IS REQUIRED

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")