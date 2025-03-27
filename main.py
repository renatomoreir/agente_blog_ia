from datetime import datetime
import os
import requests
from dotenv import load_dotenv
from blog import gerar_post, perguntar, publicar_post
from trends import tendencias_topicos

load_dotenv()

def main():

  cidade = input("Informe uma cidade para conhecer: ")

  prompt = f"{cidade} é uma cidade? responta com true ou false em formato boolean"
  if 'False' in perguntar(prompt):
    print(f" a palavra {cidade} não e reconhecida. tente novamente!")
    return

  data = input("Informe uma data em formato (dia-mês-ano) para viajar: ")

  feriado, msg = feriados(formatar_data(data))

  if feriado:
     print(msg)

  tema_viagem = f"Explorando a cidade de {cidade}"
  conteudo_post = gerar_post(tema_viagem)
  publicar_post(tema_viagem, conteudo_post)
  print("Post publicado com sucesso!")

  palavras_chave = [f"lugares turismo na cidade de {cidade}", f"lugares para realizar aventuras na cidade de {cidade}", f"melhores restaurantes na cidade de {cidade}"]
  tendencias = tendencias_topicos(palavras_chave)
  print(tendencias)


def feriados(data):
  url = os.getenv("API_FERIADO").replace('ano', data.split('-')[0])
  try:
      response = requests.get(url)
      response.raise_for_status() 
      feriados = response.json()

      if any(formatar_data(feriado['date']) == data for feriado in feriados):
        return True, f"A data {data} é feriado!"
      else:
        return False, f"A data {data} NÃO é feriado."

  except requests.exceptions.RequestException as e:
      print(f"Erro ao acessar a API: {e}")


def formatar_data(data_str):
  ### Converter a data para o formato YYYY-MM-DD.
  formatos_validos = ["%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d"]
  
  for formato in formatos_validos:
      try:
          return datetime.strptime(data_str, formato).strftime("%Y-%m-%d")
      except ValueError:
          continue 
  raise ValueError("Formato de data inválido. Use DD-MM-YYYY, DD/MM/YYYY ou YYYY-MM-DD.")


if __name__ == "__main__":
  main()


