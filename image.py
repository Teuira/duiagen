import openai
from openai import OpenAI

# Create a client
client = OpenAI(api_key="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")

# Enter your prompt from cmd
prompt = input("Enter your prompt: ")

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

print(response.data[0].url)