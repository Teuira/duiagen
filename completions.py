import openai

# Set your API key
openai.api_key = "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"

# Example function to interact with OpenAI Chat API
def generate_chat_response(prompt, model="gpt-4o"):
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    result = generate_chat_response(user_prompt)
    print("Response from OpenAI:")
    print(result)
