import streamlit as st
from data_handling import *

st.header("Bem-vindo ao Board Game Recommendation System")
st.subheader("Uma aplicação criada para ajudar você a encontrar os melhores jogos de tabuleiro com base nos seus interesses e preferências!")

st.write("### Jogos de tabuleiro:")

games_data = get_game_data()

# Format game data into a single HTML string for display
games_html = ""
for game in games_data:
    game_html = f"""<div class="game-entry">
                       <img src="{get_boardgame_image(1406)}" width="80">
                       <div>
                           <strong>{game['Nome do Jogo']}</strong><br>
                           {game['Tempo de Jogo']} horas
                       </div>
                   </div>
                   """
    games_html += game_html  # Accumulate each game entry

# Custom CSS for scrollable container and game entries
st.markdown(
    """
    <style>
    .scrollable-container {
        max-height: 200px;
        overflow-y: auto;
        padding-right: 10px; /* Prevents content from hiding under scrollbar */
    }
    .game-entry {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    .game-entry img {
        margin-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display all games within a single scrollable container
st.markdown(f'<div class="scrollable-container">{games_html}</div>', unsafe_allow_html=True)