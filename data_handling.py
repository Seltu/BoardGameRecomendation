import requests
import pandas as pd
import xml.etree.ElementTree as ET

def get_boardgame_image(game_id):
    url = f"https://boardgamegeek.com/xmlapi2/thing?id={game_id}"
    response = requests.get(url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        image_url = root.find("item/image")
        return image_url.text if image_url is not None else "No image found"
    else:
        return f"Failed to fetch data (Status Code: {response.status_code})"

game_id = 13  # Replace with the actual game ID
print(get_boardgame_image(game_id))

def get_game_data():
    return [{"Nome do Jogo":"Monopoly", "Tempo de Jogo":10}, {"Nome do Jogo":"Monopoly2", "Tempo de Jogo":10}, {"Nome do Jogo":"Monopoly2", "Tempo de Jogo":10}, {"Nome do Jogo":"Monopoly2", "Tempo de Jogo":10}, {"Nome do Jogo":"Monopoly2", "Tempo de Jogo":10} ,{"Nome do Jogo":"Monopoly2", "Tempo de Jogo":10} ,{"Nome do Jogo":"Monopoly2", "Tempo de Jogo":10}, {"Nome do Jogo":"Monopoly2", "Tempo de Jogo":10}]