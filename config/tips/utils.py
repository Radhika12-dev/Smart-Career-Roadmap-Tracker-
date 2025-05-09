import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_personalized_tips(context, roadmap_title):
    prompt = f"Give a personalized tip for {roadmap_title}. Context: {context}"
    
    try:
        # Use the correct method for OpenAI version 1.78.0
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or another model like gpt-4 if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        
        # Extract and return the generated response
        return response['choices'][0]['message']['content'].strip()
    
    except Exception as e:
        return f"Error generating tip: {str(e)}"
