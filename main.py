import openai
import os

openai.api_key = os.getenv('API_PASSWORD')

with open('prompts.txt', encoding="utf8") as file:
    data = file.read().splitlines()
    data_dict = {x.split(',')[0]: x.split(',')[1] for x in data}
    prompts_dict = {key.replace('"', ''): value.replace('"', '') for (key, value) in data_dict.items()}


user_choice = input("How would you like the chatbot to act?\n")
while True:
    msg_content = input("User: ")
    chat_response = ''

    gpt = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[
        {'role': 'system', 'content': prompts_dict[user_choice.title()]},
        {'role': 'user', 'content': msg_content},
        {'role': 'assistant', 'content': chat_response}
    ])
    chat_response = gpt.choices[0].message.content
    print(f"Chatbot: {chat_response}")
