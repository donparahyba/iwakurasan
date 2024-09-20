from atproto import Client
import google.generativeai as genai
import os

try:
    client = Client(base_url='https://bsky.social')
    client.login('iwakurasan.bsky.social', os.environ['B_API_KEY'])

    genai.configure(api_key=os.environ['G_API_KEY'])
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt_usuario = input("Insira o prompt que deseja usar: ")

    prompt_completo = f"""
    {prompt_usuario}.
    Imagine que você é a Iwakura Lain. Escreva um pensamento curto e impactante, como se fosse uma postagem em um diário digital. Seja concisa e evite detalhes excessivos. Máximo de 300 caracteres.
    """
    
    response = model.generate_content(prompt_completo)

    print(f"Texto gerado: {response.text}")
    client.send_post(response.text, langs=['pt-br'])

except Exception as e:
    print(e)