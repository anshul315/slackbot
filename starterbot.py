import os
import time
import re
import slack

slack_client = slack.WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
print(slack_client)