#chat-gpt --> averiguando valores
import openai
import os
from dotenv import load_dotenv

class ChatBot:
    def message(content):
        # Carregue as variáveis de ambiente do arquivo .env
        load_dotenv()
        openai.api_key = os.getenv("key-openai")

        MODEL = "gpt-3.5-turbo"
        
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": f"{content}"},
            ],
            temperature=0,
        )

        return response.choices[0].message.content

