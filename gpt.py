import openai

openai.api_key = "sk-proj-rrNel6sj8Mig61KeRygmT3BlbkFJd3Y0aiqbmsaJMVoXfQ7N"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content":prompt}]
    )
    
    return response.choices[0].message.content.strip()