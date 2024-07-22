import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime
import schedule

# 1. Função para consultar o preço do produto


def consultar_preco(url):
    try:
        # Fazer a requisição para o site
        response = requests.get(url)
        response.raise_for_status()  # Lança exceção se houver erro de status

        # Analisar o conteúdo HTML com BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar o elemento HTML que contém o preço
        preco_element = soup.find(
            's', class_='samsungbr-app-pdp-2-x-slashedPrice')  # Classe correta!

        # Extrair o valor numérico do preço
        preco_texto = preco_element.text.strip()
        preco = float(preco_texto.replace(
            'R$', '').replace('.', '').replace(',', '.'))

        return preco

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return None  # Retorna None em caso de erro


# 2. Função para atualizar a planilha
def atualizar_planilha(nome_produto, preco, link, data):
    try:
        # Crie a planilha se ela não existir
        try:
            planilha = pd.read_csv('precos.csv')
        except FileNotFoundError:
            planilha = pd.DataFrame(
                columns=['Produto', 'Data', 'Valor', 'Link'])

        # Adicione a nova linha à planilha
        nova_linha = {'Produto': nome_produto,
                      'Data': data, 'Valor': preco, 'Link': link}
        planilha = planilha.append(nova_linha, ignore_index=True)

        # Salve a planilha (em formato CSV)
        planilha.to_csv('precos.csv', index=False)

    except Exception as e:
        print(f"Erro ao atualizar a planilha: {e}")

# 3. Função principal que executa o script


def main():
    # Configure o nome do produto, o URL do produto e o link para o produto
    # Último lançamento da Samsung (verifique o nome exato)
    nome_produto = 'Samsung Galaxy S24 Ultra'
    # Substitua pelo URL do site
    url_produto = 'https://www.samsung.com/br/smartphones/galaxy-s24-ultra/'
    link = url_produto

    # Obter a data atual
    data = datetime.datetime.now().strftime('%Y-%m-%d')

    # Consultar o preço do produto
    preco = consultar_preco(url_produto)

    # Se o preço foi encontrado, criar a planilha se não existir e atualizar
    if preco:
        atualizar_planilha(nome_produto, preco, link, data)
        print(f"Preço do {nome_produto} atualizado em {data}: R${preco:.2f}")
    else:
        print(f"Não foi possível encontrar o preço do {
              nome_produto} em {data}.")


# 4. Agendar a execução do script a cada 30 minutos
schedule.every(30).minutes.do(main)

# Executar o script de forma contínua
while True:
    schedule.run_pending()
    time.sleep(1)
