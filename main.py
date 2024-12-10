import streamlit as st
from data_handling import *
from state_manager import *

st.header("Bem-vindo ao Board Game Recommendation System")
st.subheader("Uma aplicação criada para ajudar você a encontrar os melhores jogos de tabuleiro com base nos seus interesses e preferências!")

st.write("### Jogos de tabuleiro:")

# Configurações
games_data = get_game_data()  # Lista de todos os jogos
games_per_page = 5  # Número de jogos por página

# Inicializa o estado da página
initialize_page_state(st.session_state)

# Obtém a página atual
current_page = get_current_page(st.session_state)

# Determina os índices dos jogos a serem exibidos na página atual
start_index = current_page * games_per_page
end_index = start_index + games_per_page
current_page_games = games_data[start_index:end_index]

# Formata os jogos da página atual em HTML
games_html = ""
for game in current_page_games:
    game_html = f"""<div class="game-entry">
                       <img src="{get_boardgame_image(game['ID'])}" width="80">
                       <div>
                           <strong>{game['Nome do Jogo']}</strong><br>
                           {game['Tempo de Jogo']} horas
                       </div>
                   </div>
                   """
    games_html += game_html

# Custom CSS para o contêiner scrollável e os itens do jogo
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

# Exibe a página atual
st.markdown(f'<div class="scrollable-container">{games_html}</div>', unsafe_allow_html=True)

# Botões de navegação
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("Anterior"):
        prev_page(st.session_state)
with col3:
    if st.button("Próximo"):
        next_page(st.session_state, len(games_data), games_per_page)