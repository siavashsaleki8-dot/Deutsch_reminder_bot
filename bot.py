import os
import random
import requests
from datetime import datetime

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "-4753385536"

TOPICS = [
    {
        "title": "Arbeit und Beruf",
        "questions": [
            "Welche Eigenschaften sollte ein guter Mitarbeiter haben?",
            "Ist Geld wichtiger als Arbeitszufriedenheit?",
            "Sollte man den Beruf mehrmals wechseln?",
            "Welche Rolle spielt Teamarbeit?"
        ],
        "vocabulary": [
            "die Bewerbung",
            "die Arbeitslosigkeit",
            "die Beförderung",
            "das Gehalt",
            "die Verantwortung",
            "die Qualifikation",
            "der Kollege",
            "der Arbeitgeber"
        ],
        "redemittel": [
            "Meiner Meinung nach ...",
            "Ich bin davon überzeugt, dass ...",
            "Ein wichtiger Vorteil ist ...",
            "Andererseits darf man nicht vergessen, dass ..."
        ],
        "grammar": "Konjunktiv II"
    },

    {
        "title": "Umweltschutz",
        "questions": [
            "Welche Umweltprobleme gibt es?",
            "Wie kann jeder Mensch die Umwelt schützen?",
            "Sollte Plastik verboten werden?",
            "Welche Verantwortung haben Unternehmen?"
        ],
        "vocabulary": [
            "die Nachhaltigkeit",
            "der Klimawandel",
            "die Umweltverschmutzung",
            "erneuerbare Energie",
            "recyceln",
            "Müll trennen",
            "CO₂-Ausstoß",
            "Ressourcen"
        ],
        "redemittel": [
            "Ich vertrete die Auffassung, dass ...",
            "Es steht außer Frage, dass ...",
            "Außerdem sollte man berücksichtigen ..."
        ],
        "grammar": "Passiv"
    },

    {
        "title": "Gesunde Ernährung",
        "questions": [
            "Was bedeutet gesunde Ernährung?",
            "Kochen Sie lieber selbst?",
            "Wie oft essen Sie Fast Food?",
            "Sollten Schulen gesundes Essen anbieten?"
        ],
        "vocabulary": [
            "ausgewogen",
            "die Vitamine",
            "das Eiweiß",
            "die Ernährung",
            "ungesund",
            "Bio-Produkte",
            "die Kalorien"
        ],
        "redemittel": [
            "Ich lege großen Wert auf ...",
            "Aus gesundheitlicher Sicht ..."
        ],
        "grammar": "Relativsätze"
    },

    {
        "title": "Digitale Medien",
        "questions": [
            "Wie wichtig sind soziale Medien?",
            "Welche Nachteile haben Smartphones?",
            "Sollte die Bildschirmzeit begrenzt werden?",
            "Wie beeinflusst das Internet unser Leben?"
        ],
        "vocabulary": [
            "die Privatsphäre",
            "der Datenschutz",
            "online",
            "die App",
            "das Netzwerk",
            "die Information",
            "kommunizieren"
        ],
        "redemittel": [
            "Ich halte es für sinnvoll, dass ...",
            "Meines Erachtens ..."
        ],
        "grammar": "obwohl / trotzdem"
    },

    {
        "title": "Reisen",
        "questions": [
            "Warum reisen Menschen?",
            "Hotel oder Ferienwohnung?",
            "Welche Reise war unvergesslich?",
            "Ist nachhaltiger Tourismus wichtig?"
        ],
        "vocabulary": [
            "der Urlaub",
            "die Unterkunft",
            "die Sehenswürdigkeit",
            "die Kultur",
            "die Reiseversicherung",
            "der Flug"
        ],
        "redemittel": [
            "Ich würde gern erwähnen, dass ...",
            "Besonders wichtig finde ich ..."
        ],
        "grammar": "Präteritum und Perfekt"
    }
]

GRAMMAR_CHALLENGES = [
    "Benutzen Sie mindestens zwei Passivsätze.",
    "Verwenden Sie drei Konnektoren (obwohl, trotzdem, während).",
    "Benutzen Sie Konjunktiv II.",
    "Verwenden Sie mindestens zwei Relativsätze.",
    "Benutzen Sie Futur I.",
    "Verwenden Sie indirekte Rede."
]

WRITING_TASKS = [
    "Schreiben Sie eine Stellungnahme (120 Wörter).",
    "Bereiten Sie einen 3-minütigen Vortrag vor.",
    "Diskutieren Sie das Thema mit einem Partner.",
    "Nennen Sie Vor- und Nachteile.",
    "Geben Sie Beispiele aus Ihrem Alltag."
    
]
def choose_topic():
    return random.choice(TOPICS)


def create_message():
    topic = choose_topic()

    message = "🇩🇪 Deutsch mit Saleki B2\n\n"
    message += f"📌 Thema: {topic['title']}\n\n"

    message += "🗣 Fragen:\n"
    for i, q in enumerate(topic["questions"], 1):
        message += f"{i}. {q}\n"

    message += "\n📚 Wortschatz:\n"
    for word in topic["vocabulary"]:
        message += f"• {word}\n"

    message += "\n💬 Redemittel:\n"
    for phrase in topic["redemittel"]:
        message += f"• {phrase}\n"

    message += "\n✍️ Grammatik-Challenge:\n"
    message += f"• {topic['grammar']}\n"
    message += f"• {random.choice(GRAMMAR_CHALLENGES)}\n"

    message += "\n📝 ÖSD B2 Aufgabe:\n"
    message += f"• {random.choice(WRITING_TASKS)}\n"

    message += "\n⏰ "
    message += datetime.now().strftime("%d.%m.%Y")

    return message


def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    response = requests.post(url, data=data)

    return response.json()


def main():
    message = create_message()
    result = send_message(message)

    print(result)


if __name__ == "__main__":
    main()
    MORE_TOPICS = [
    {
        "title": "Bildung und lebenslanges Lernen",
        "questions": [
            "Warum ist Weiterbildung wichtig?",
            "Sollte man immer neue Fähigkeiten lernen?",
            "Welche Rolle spielt Online-Lernen?",
            "Welche Erfahrungen haben Sie gemacht?"
        ],
        "vocabulary": [
            "die Weiterbildung",
            "die Fähigkeit",
            "die Ausbildung",
            "die Erfahrung",
            "sich weiterentwickeln"
        ],
        "redemittel": [
            "Ich bin der Ansicht, dass ...",
            "Ein entscheidender Punkt ist ..."
        ],
        "grammar": "Nominalisierung"
    },

    {
        "title": "Migration und Integration",
        "questions": [
            "Welche Herausforderungen haben Migranten?",
            "Welche Rolle spielt Sprache bei Integration?",
            "Was kann die Gesellschaft tun?",
            "Welche Vorteile hat kulturelle Vielfalt?"
        ],
        "vocabulary": [
            "die Integration",
            "die Vielfalt",
            "die Sprache",
            "die Gesellschaft",
            "die Gleichberechtigung"
        ],
        "redemittel": [
            "Ein wichtiger Aspekt ist ...",
            "Man darf nicht außer Acht lassen, dass ..."
        ],
        "grammar": "Nebensätze"
    },

    {
        "title": "Technologie der Zukunft",
        "questions": [
            "Wie verändert Technologie unser Leben?",
            "Welche Chancen bietet künstliche Intelligenz?",
            "Welche Risiken gibt es?",
            "Wie sieht die Zukunft aus?"
        ],
        "vocabulary": [
            "die Innovation",
            "die Entwicklung",
            "die Automatisierung",
            "die Digitalisierung",
            "der Fortschritt"
        ],
        "redemittel": [
            "Langfristig gesehen ...",
            "Es ist davon auszugehen, dass ..."
        ],
        "grammar": "Futur I"
    },

    {
        "title": "Wohnen und Stadtleben",
        "questions": [
            "Lieber Stadt oder Land?",
            "Welche Probleme gibt es in Großstädten?",
            "Wie wichtig ist bezahlbarer Wohnraum?",
            "Wie sieht Ihre Traumwohnung aus?"
        ],
        "vocabulary": [
            "die Miete",
            "der Wohnraum",
            "die Nachbarschaft",
            "die Infrastruktur",
            "die Lebensqualität"
        ],
        "redemittel": [
            "Was diesen Punkt betrifft ...",
            "Ein Vorteil beziehungsweise Nachteil ist ..."
        ],
        "grammar": "Vergleichsformen"
    }
]


# Erweiterung der Themenliste
TOPICS.extend(MORE_TOPICS)


# Vermeidung von direkten Wiederholungen
last_topic = None


def choose_topic():
    global last_topic

    available = [
        topic for topic in TOPICS
        if topic["title"] != last_topic
    ]

    selected = random.choice(available)
    last_topic = selected["title"]

    return selected
