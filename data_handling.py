import requests
import pandas as pd
import difflib
import xml.etree.ElementTree as ET

def get_boardgame_image(game_id):
    try:
        url = f"https://boardgamegeek.com/xmlapi2/thing?id={game_id}"
        response = requests.get(url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            image_url = root.find("item/image")
            return image_url.text if image_url is not None else "No image found"
        else:
            return f"Failed to fetch data (Status Code: {response.status_code})"
    except Exception:
        return "https://ih1.redbubble.net/image.4905811447.8675/flat,750x,075,f-pad,750x1000,f8f8f8.jpg"

def get_game_data():
    # Lê o arquivo CSV e trata vírgulas como separadores decimais
    df = pd.read_csv('bgg_dataset.csv', sep=';', decimal=',')

    # Imprime os nomes das colunas para verificar se estão corretos
    print(df.columns)

    # Converte o DataFrame em uma lista de dicionários
    game_data = df.to_dict(orient='records')

    return game_data

def sort_games_by_query(games_data, query):
    if not query.strip():
        return games_data  # Retorna sem ordenação se a consulta estiver vazia

    # Adiciona uma pontuação de similaridade para cada jogo
    scored_games = [
        {
            **game,
            "similarity_score": difflib.SequenceMatcher(None, query.lower(), game['Name'].lower()).ratio()
        }
        for game in games_data
    ]

    # Ordena os jogos pela pontuação de similaridade (maior primeiro)
    sorted_games = sorted(scored_games, key=lambda x: x['similarity_score'], reverse=True)
    return sorted_games