import openai

openai.api_key = "your-api-key"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]  # Fixed 'messages' and 'user' role
    )
    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break  # Fixed exit command

        response = chat_with_gpt(user_input)  # Fixed typo 'respone' to 'response'
        print("Chatbot:", response)
