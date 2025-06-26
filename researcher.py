from transformers import pipeline
from config import HUGGINGFACE_API_KEY

# research_pipeline = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", token=HUGGINGFACE_API_KEY)
# research_pipeline = pipeline("text-generation", model="facebook/opt-350m", token=HUGGINGFACE_API_KEY)
research_pipeline = pipeline("text-generation", model="facebook/opt-350m", token=HUGGINGFACE_API_KEY, device_map="auto")
""" research_pipeline = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.1", 
    token=HUGGINGFACE_API_KEY,
    device_map="auto"
) """

""" research_pipeline = pipeline(
    "text-generation",
    model="facebook/opt-1.3b",  # Daha küçük model
    token=HUGGINGFACE_API_KEY,
    device_map="auto"
) """


def collect_research_data(topic):
    """
    Verilen konu hakkında araştırma verilerini toplar.
    """
    try:
        prompt = (
            f"Provide a detailed, factual research summary about {topic}. "
            "Include key statistics, recent advancements, and expert opinions. "
            "Structure it as a professional research document without conversational elements."
        )

        response = research_pipeline(
            prompt, 
            max_length=800,  
            num_return_sequences=1,  
            truncation=True,  
            temperature=0.5,
            top_p=0.9,  
            do_sample=True,  
            repetition_penalty=1.3
        )

        """ response = research_pipeline(
            prompt, 
            max_length=1024,  
            num_return_sequences=1,  
            truncation=True,  
            temperature=0.3,
            top_p=0.85,  
            do_sample=True,  
            repetition_penalty=1.5
        ) """

        research_data = response[0]["generated_text"].strip()
        return research_data

    except Exception as e:
        print(f"Error while collecting research data: {e}")
        return None

