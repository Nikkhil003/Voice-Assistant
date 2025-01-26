import openai

openai.api_key = "your_openai_api_key"

def ask_gpt(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=100
    )
    return response.choices[0].text.strip()