# ChatGPT in 20 seconds
> The main code is borrowed from [my friend's repo](https://github.com/shinan6/ChatGPT-API-version). I make minor modifications to make it more user-friendly. The README will walk you through step by step.

### Notes:
- This tool is based on `gpt-3.5-turbo`, release by OpenAI on Feb 28, 2023.
- It is more powerful than the free version in https://chat.openai.com/chat.
- Here is the charge (seems cheap!): `$0.002 / 1K tokens`.
### Play in 20 seconds:
- **Step 1: register OpenAI account (10 seconds)**
    - fill in your payment https://platform.openai.com/account/billing/
    - request an API key https://platform.openai.com/account/api-keys/

- **Step 2: setup the environment (5 seconds)**
    ```bash
    pip install openai
    git clone https://github.com/ycq091044/ChatGPT-in-20-seconds
    ```

- **Step 3: Update information (5 seconds)**
    - update `openai.api_key` and `root` in `chatgpt.py`

- **Step 4: play in the terminal**
    ```bash
    python chatgpt.py
    ```

### Demo
```
%%% python chatgpt.py

Welcome to terminal ChatGPT, type "exit" to quit.
Chat history will be saved in the /Users/chaoqiyang/Desktop/chatgpt folder.

[User]: if a user like a repo, will they give a star⭐?

[ChatGPT]: Yes, when a user likes a repo on GitHub, they can give it a star⭐,
which is a form of social endorsement or bookmarking. This enables other users 
to discover popular or useful repos, and also allows the user to keep track of 
the repos they like or want to follow.
``` 