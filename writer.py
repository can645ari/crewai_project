import os

def write_article(research_data, topic, output_dir="output"):
    """
    Araştırma verilerini Markdown formatında kaydeder.
    """
    if research_data is None or len(research_data) < 50:  # Çok kısa ve anlamsız verileri engelle
        print("⚠ No valid research data found, cannot write article.")
        return
    
    try:
        formatted_topic = topic.replace(" ", "_").lower()
        output_file = os.path.join(output_dir, f"{formatted_topic}_report.md")
        
        article_content = f"# Research Article on {topic}\n\n"
        article_content += f"## Introduction\n\n{topic} is an important topic in today's world. Here is an overview based on the latest research.\n\n"
        article_content += f"## Research Data\n\n{research_data}\n\n"
        article_content += f"## Conclusion\n\nBased on the research, {topic} is evolving with new advancements and insights."

        os.makedirs(output_dir, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(article_content)
        
        print(f"Article written to {output_file}")
    
    except Exception as e:
        print(f"Error while writing the article: {e}")
