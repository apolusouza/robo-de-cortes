from google.colab import userdata
import json
import re

API_NOTION = userdata.get('API_NOTION')

from decorator import append
import requests
import json

data_base_id = 'ffa074382aee4689a996778a26d6fdb3'
data_source_id= '7830ab9a-b820-4601-b2a4-8d14583a01eb'

url_data_base = f"https://api.notion.com/v1/databases/{data_base_id}"
source_id = f"https://api.notion.com/v1/data_sources/{data_source_id}/query"

payload = {
    "filter": {
        "property": "status", # O nome da sua coluna no Notion
        "status": {           # O tipo da coluna
            "equals": "Construção" # A condição exata que você quer
        }
    },
    "page_size":10
}

headers = {
    "Notion-Version": "2026-03-11",
    "Authorization": f"Bearer {API_NOTION}"
}

response = requests.post(source_id, json=payload, headers=headers)

json_pages = response.json()

textos = []
i = 0

for page in json_pages['results']:
  textos.append(page['properties']['Texto revisado']['rich_text'])
  i +=1

conteudo = ''

#from IPython.utils import text

for texto in textos[0]:
  conteudo += texto['text']['content']

try:
  regex = r'POST\s\d|POST\d\d'
  resultado = re.findall(regex, conteudo)
except Exception as e:
  print(f'Formatação errada')
  print(f'Erro:{e}')

split_conteudo = conteudo.split('\n')

i = 0
while len(resultado) > i:
  split_conteudo.remove(resultado[i])
  i += 1

for item in split_conteudo:
  print(item)