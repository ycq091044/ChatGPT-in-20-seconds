import openai
import csv
import os

# put your openai api key here
openai.api_key = ""

# the root directory of the chat history, default is the current directory
root = "."

def get_response(chat):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat
    )
    return response["choices"][0]["message"]["content"]

MSG = """
Welcome to terminal ChatGPT, type "exit" to quit.
- history will be saved in the {} folder
""".format(root)

def main():
    history = []

    while True:
        user_input = input("[User]: ").strip()
        print()
        if user_input == "exit":
            with open(f"{root}/history/{len(os.listdir(root + '/history'))+1}.csv", mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["role", "content"])
                writer.writeheader()
                for row in history:
                    writer.writerow(row)
            exit()
        history.append({"role": "user", "content": user_input})
        rsp_content = get_response(history)
        print(f'[ChatGPT]: {rsp_content}\n')
        history.append({"role": "chatgpt", "content": rsp_content})

if __name__ == "__main__":
    if not os.path.exists(root + '/history'):
        os.makedirs(root + '/history') 
    
    print (MSG)
    main()
