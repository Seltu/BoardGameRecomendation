import streamlit as st
from data_handling import *
from state_manager import *
from config import *

st.header("Bem-vindo ao Board Game Recommendation System")
st.subheader("Uma aplicação criada para ajudar você a encontrar os melhores jogos de tabuleiro com base nos seus interesses e preferências!")

st.write("### Lista de Jogos de Tabuleiro:")

input_query(st.text_input("Pesquise por um jogo de tabuleiro"))

# Inicializa o estado da página
initialize_state()
games_data = get_games_data()

query = get_query()
if query != "":
    games_data = sort_games_by_query(get_games_data(), query)

# Obtém a página atual
current_page = get_current_page()

# Determina os índices dos jogos a serem exibidos na página atual
start_index = current_page * games_per_page
end_index = start_index + games_per_page
current_page_games = games_data[start_index:end_index]

# Exibe os jogos e botões de adição à lista
for game in current_page_games:
    col1, col2, col3 = st.columns([3, 4, 4])

    with col1:
        st.image(get_boardgame_image(game['ID']), width=80)

    with col2:
        st.write(f"**{game['Name']}**")
        st.write(f"{game['Play Time']} horas")

    with col3:
        if st.button(f"Adicionar à minha lista {game['Name']}", key=game['ID']):
            # Adiciona o jogo à lista de favoritos
            st.session_state.favorite_games.append(game)
            st.success(f"Jogo '{game['Name']}' adicionado à sua lista!")

# Botões de navegação (exibidos apenas quando necessário)
st.write(f"Página {current_page+1}/{get_max_page()+1}")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if current_page > 0:  # Exibe o botão "Anterior" apenas se não estiver na primeira página
        if st.button("Anterior"):
            prev_page()
            st.rerun()

with col3:
    if end_index < len(games_data):  # Exibe o botão "Próximo" apenas se houver mais páginas
        if st.button("Próximo"):
            next_page()
            st.rerun()

# Exibe a lista de jogos favoritos
st.write("### Seus Jogos Favoritos:")
for game in st.session_state.favorite_games:
    st.write(f"- {game['Name']}")