import requests
import random

TOKEN = 8629996047:AAHddPLE0z8_VVHimoWp58E1-5AUJ3So3Hw
CHAT_ID = "-4753385536"

topics = [
    "Mein Wochenende",
    "Meine Familie",
    "Meine Arbeit",
    "Meine Reise",
    "Meine Ziele"
]

topic = random.choice(topics)

message = f"""🇩🇪 Zeit zum Sprechen!

Thema des Tages:
{topic}

Sprich 2 Minuten Deutsch und sende eine Sprachnachricht 🎤
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
