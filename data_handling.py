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
    return [
        {"ID": 1406, "Nome do Jogo": "Catan", "Tempo de Jogo": 1.5},
        {"ID": 2004, "Nome do Jogo": "Pandemic", "Tempo de Jogo": 2},
        {"ID": 1546, "Nome do Jogo": "Ticket to Ride", "Tempo de Jogo": 1.5},
        {"ID": 3456, "Nome do Jogo": "Gloomhaven", "Tempo de Jogo": 3},
        {"ID": 9087, "Nome do Jogo": "Terraforming Mars", "Tempo de Jogo": 2.5},
        {"ID": 1234, "Nome do Jogo": "7 Wonders", "Tempo de Jogo": 1},
        {"ID": 6789, "Nome do Jogo": "Dominion", "Tempo de Jogo": 0.75},
        {"ID": 8765, "Nome do Jogo": "Agricola", "Tempo de Jogo": 2.5},
        {"ID": 4567, "Nome do Jogo": "Carcassonne", "Tempo de Jogo": 1},
        {"ID": 3452, "Nome do Jogo": "Puerto Rico", "Tempo de Jogo": 2},
        # Adicione mais jogos conforme necessário
    ]