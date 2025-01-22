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