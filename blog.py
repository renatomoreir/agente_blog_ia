import google.generativeai as genai
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
WORDPRESS_USERNAME = os.getenv("WORDPRESS_USERNAME")
WORDPRESS_PASSWORD = os.getenv("WORDPRESS_PASSWORD")
WORDPRESS_URL = os.getenv("WORDPRESS_URL")

genai.configure(api_key=GEMINI_API_KEY)
wp = Client(WORDPRESS_URL, WORDPRESS_USERNAME, WORDPRESS_PASSWORD)

def gerar_post(tema):
    ###Gera um post de blog usando o Gemini
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"Escreva um post de blog sobre viagens com o tema: {tema}. Inclua título, introdução, dicas, fotos, restaurantes e conclusão."
    response = model.generate_content(prompt)
    return response.text

def publicar_post(titulo, conteudo):
    ###Publica o post no WordPress
    post = WordPressPost()
    post.title = titulo
    post.content = conteudo
    post.terms_names = {
        'post_tag': ['viagem', 'aventura', 'turismo'],
        'category': ['Destinos']
    }
    post.post_status = 'publish'
    wp.call(NewPost(post))


def perguntar(prompt):
  model = genai.GenerativeModel('gemini-2.0-flash')
  response = model.generate_content(prompt)
  return response.text
