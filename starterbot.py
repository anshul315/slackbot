import os
import time
import re
import slack
from dotenv import load_dotenv
load_dotenv()

slack_client = slack.WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

response = slack_client.chat_postMessage(
        channel='#random',
        text="Hello world!")
assert response["ok"]
assert response["message"]["text"] == "Hello world!"
    
print(slack_client)