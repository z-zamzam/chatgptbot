import openai
import os

openai.api_key = os.environ['API_KEY']

# Retrieving the prompts and cleaning up the data into a usable format
with open('prompts.txt', encoding="utf8") as file:
    data = file.read().splitlines()
    data_dict = {x.split(',')[0]: x.split(',')[1] for x in data}
    prompts_dict = {key.replace('"', ''): value.replace('"', '') for (key, value) in data_dict.items()}

# Setting the bot's behavior by using an input and selecting the prompt accordingly
user_choice = input("How would you like the chatbot to act?\n")

# Setting up the loop for chatting with the bot
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
