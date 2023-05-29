import openai
import os
openai.api_base = "http://localhost:4891/v1"
from constants import models, tools

#openai.api_base = "https://api.openai.com/v1"

openai.api_key = os.environ["OPENAI_API_KEY"]

# Set up the prompt and other parameters for the API request
prompt = "Who is Michael Jordan?"


# Make the API request
response = openai.Completion.create(
    model=models[0],
    prompt=prompt,
    max_tokens=50,
    temperature=0.28,
    top_p=0.95,
    n=1,
    echo=True,
    stream=False
)

# Print the generated completion
print(response)