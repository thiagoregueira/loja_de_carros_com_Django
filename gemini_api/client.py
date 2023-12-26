import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()


def get_car_ai_bio(model, brand, year):
    contents = """
    Me mostre uma descrição de venda para o carro {}, {}, {}, em português e em apenas 250 caracteres. Fale coisas específicas desse modelo de carro.
    """

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    contents = contents.format(brand, model, year)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(
        contents=contents,
    )
    return response.text
