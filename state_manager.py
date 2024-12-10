import streamlit
from streamlit import session_state
from config import *

def input_query(query):
    if query == "":
        return
    if 'query' not in session_state:
        session_state['query'] = query
    elif session_state['query'] != query:
        session_state['query'] = query
        set_page(0)
        streamlit.rerun()

def get_query():
    if 'query' in session_state:
        return session_state['query']
    else:
        return ""

def initialize_state():
    """
    Inicializa o estado da página no Streamlit, caso ainda não tenha sido criado.
    """
    if 'page' not in session_state:
        session_state['page'] = 0
    if 'games_data' not in session_state:
        session_state['games_data'] = get_game_data()
    if "favorite_games" not in session_state:
        session_state.favorite_games = []

def get_current_page():
    """
    Retorna a página atual armazenada no estado da sessão.
    """
    return session_state['page']


def set_page(page):
    """
    Define a página atual no estado da sessão.
    """
    session_state['page'] = page


def next_page():
    """
    Incrementa a página atual no estado da sessão, se possível.
    """
    max_page = (len(get_games_data()) - 1) // games_per_page
    if session_state['page'] < max_page:
        session_state['page'] += 1


def prev_page():
    """
    Decrementa a página atual no estado da sessão, se possível.
    """
    if session_state['page'] > 0:
        session_state['page'] -= 1

def get_max_page():
    return (len(get_games_data()) - 1) // games_per_page

def get_games_data():
    return session_state['games_data']