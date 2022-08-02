import os
from slack_bolt import App
from dotenv import load_dotenv
from pathlib import Path
import random

# loads env variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Initializes app with bot token and signing secret
app = App(
    token=os.environ['SLACK_BOT_TOKEN'],
    signing_secret=os.environ['SLACK_SIGNING_SECRET']
)

# functionality
@app.event("app_mention")
def event_test(body, say):
    print(body)
    user_id = body["event"]["user"]
    if "random number" in body["event"]["text"].lower():
        say("Here's a random number: " + str(random.randint(1,100)))
    else:
        say("Hello <@" + user_id + ">!")

# Starts app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
