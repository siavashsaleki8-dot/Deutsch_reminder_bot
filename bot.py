import os
import json
import random
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

with open("topics.json", "r", encoding="utf-8") as file:
    topics = json.load(file)

lesson = random.choice(topics)

message = f"""🇩🇪 Deutsch mit Saleki

🎯 Sprechtraining B2

📌 Thema:
{lesson['title']}

🗣️ Leitfragen:

"""

for i, question in enumerate(lesson["questions"], 1):
    message += f"{i}. {question}\n"

message += "\n📚 Wortschatz:\n"

for word in lesson["vocabulary"]:
    message += f"• {word}\n"

message += "\n💬 Redemittel:\n"

for phrase in lesson["redemittel"]:
    message += f"• {phrase}\n"

message += f"""

📝 Grammatik-Challenge:
{lesson['grammar']}

🎤 Bitte schicken Sie heute eine Sprachnachricht (3–5 Minuten).
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
