import os
from researcher import collect_research_data
from writer import write_article

def main():
    """
    Ana fonksiyon, kullanıcıdan konu alır, araştırma verilerini toplar ve makale yazar.
    """
    # Kullanıcıdan konu al
    topic = input("Enter the topic for the article: ")

    # Araştırma verilerini topla
    print(f"Collecting research data for the topic: {topic}")
    research_data = collect_research_data(topic)

    # Araştırma verisi varsa makale yaz
    if research_data:
        print(f"Writing article for topic: {topic}")
        write_article(research_data, topic)
    else:
        print("No research data found, cannot proceed with writing the article.")

if __name__ == "__main__":
    main()
