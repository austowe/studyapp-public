import os
import json
import time
import openai
import random
import keys

cwd = os.getcwd()
f = open(os.path.join(cwd, "questions.json"))
questions = json.load(f)

shuffle = input("Would you like shuffle the questions in a random order? (y/n) ").lower()
if shuffle == 'y':
    random.shuffle(questions['questions'])
print('\n\n')
for i in questions['questions']:
    response = input(i['text'] + '\n\n').upper()
    if response == i['answer']:
        print('Correct!\n')
    else:
        print('Incorrect! Loading information...')
        messages=[
            {"role": "system", "content": "You are an assistant that helps with test preparation reviews. Make your response short."},
        ]
        openai.organization = keys.openai_org
        openai.api_key = keys.openai_api_key
        messages.append({"role": "user", "content": "Tell me why the correct answer is not " + response + " and share why " + i['answer'] + " is the correct response to the following question:" + i['text']})
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=messages
        )
        chat_response = chat_completion['choices'][0]['message']['content']
        print("\n" + chat_response + "\n")
    time.sleep(2)

print('\nFinished!')