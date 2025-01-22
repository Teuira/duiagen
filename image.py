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
