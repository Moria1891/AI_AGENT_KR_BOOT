import os
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

# First, handle the command-line arguments and define 'prompt'
if len(sys.argv) < 2:
    print("Usage: python main.py <prompt>")
    sys.exit(1)

prompt_args = [arg for arg in sys.argv[1:] if arg != "--verbose"]
prompt = " ".join(prompt_args)

# Now that 'prompt' is defined, you can create the 'messages' list
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)
print(response.text)

prompt_token = response.usage_metadata.prompt_token_count
response_token = response.usage_metadata.candidates_token_count


if "--verbose" in sys.argv:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {prompt_token}\nResponse tokens: {response_token}")
