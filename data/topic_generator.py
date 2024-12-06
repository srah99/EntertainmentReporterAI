import random

def generate_topic(data):
    topics = []
    for item in data["artists"]:
        topic = f"The Evolution of {item['name']}'s Music Style"
        topics.append(topic)
    return random.choice(topics)

def generate_topic_wikipedia(data):
    topics = []
    for page in data["query"]["pages"].values():
        topic = f"The History of {page['title']}"
        topics.append(topic)
    return random.choice(topics)

def generate_topic_news(data):
    topics = []
    for article in data["articles"]:
        topic = f"{article['title']} - A New Era in Rock Music?"
        topics.append(topic)
    return random.choice(topics)
