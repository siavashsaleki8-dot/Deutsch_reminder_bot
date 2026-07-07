import os
import requests
import random

TOKEN = os.environ[8629996047:AAHddPLE0z8_VVHimoWp58E1-5AUJ3So3Hw ]
CHAT_ID = os.environ["CHAT_ID"]

topics = [
    "Mein Wochenende",
    "Meine Familie",
    "Meine Arbeit",
    "Meine Reise",
    "Meine Ziele",
    "Mein Lieblingsfilm"
]

topic = random.choice(topics)

message = f"""🇩🇪 Zeit zum Sprechen!

Thema des Tages:
{topic}

Sprich 2 Minuten auf Deutsch und sende eine Sprachnachricht 🎤
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
