from data_handling import *

def manhattan(user, game):
    """Computes the Manhattan distance. """
    distance = 0
    total = 0
    for key in user:
        if key in game:
            distance += abs(user[key] - game[key])
            total += 1
    return distance


def recommend(favorites, games, keys_to_normalize):
    """Recommends games based on the average distance to a list of favorite games."""
    games = [item for item in games if item not in favorites]

    # Normalizar o conjunto de jogos e obter os limites de normalização
    games, min_max = normalize_data(games, keys_to_normalize)

    # Normalizar os jogos favoritos usando os mesmos limites
    favorites = normalize_user_games(favorites, min_max, keys_to_normalize)

    distances = []

    for game in games:
        total_distance = 0
        # Calcular a distância entre o jogo atual e todos os jogos favoritos
        for favorite_game in favorites:
            favorite_game = {chave: favorite_game[chave] for chave in keys_to_normalize if chave in favorite_game}
            distance = manhattan(favorite_game, game)
            total_distance += distance
        # Calcular a média das distâncias para todos os jogos favoritos
        average_distance = total_distance / len(favorites)
        distances.append((average_distance, game))

    # Ordenar pela média das distâncias (menor é melhor)
    distances.sort(key=lambda x: x[0])
    return distances

def normalize_data(games, keys_to_normalize):
    """Normalize numerical values in the dataset."""
    # Calcular os mínimos e máximos
    min_max = {key: (float('inf'), float('-inf')) for key in keys_to_normalize}
    for game in games:
        for key in keys_to_normalize:
            if key in game:
                min_max[key] = (
                    min(min_max[key][0], game[key]),
                    max(min_max[key][1], game[key]),
                )

    # Normalizar os valores
    def normalize_game(game, min_max):
        normalized_game = game.copy()  # Evitar alterar o original
        for key in keys_to_normalize:
            if key in game:
                min_val, max_val = min_max[key]
                if max_val > min_val:  # Evitar divisão por zero
                    normalized_game[key] = (game[key] - min_val) / (max_val - min_val)
                else:
                    normalized_game[key] = 0  # Se todos os valores forem iguais
        return normalized_game

    return [normalize_game(game, min_max) for game in games], min_max


def normalize_user_games(user_games, min_max, keys_to_normalize):
    """Normalize user games using the same min-max values as the dataset."""
    def normalize_game(game, min_max):
        normalized_game = game.copy()
        for key in keys_to_normalize:
            if key in game:
                min_val, max_val = min_max[key]
                if max_val > min_val:
                    normalized_game[key] = (game[key] - min_val) / (max_val - min_val)
                else:
                    normalized_game[key] = 0
        return normalized_game

    return [normalize_game(game, min_max) for game in user_games]


# Variáveis numéricas a normalizar
keys_to_normalize = [
    "Min Players", "Max Players", "Play Time", "Min Age",
    "Rating Average", "BGG Rank", "Complexity Average"
]