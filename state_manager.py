def initialize_page_state(session_state, key='page', initial_value=0):
    """
    Inicializa o estado da página no Streamlit, caso ainda não tenha sido criado.
    """
    if key not in session_state:
        session_state[key] = initial_value


def get_current_page(session_state, key='page'):
    """
    Retorna a página atual armazenada no estado da sessão.
    """
    return session_state[key]


def set_page(session_state, page, key='page'):
    """
    Define a página atual no estado da sessão.
    """
    session_state[key] = page


def next_page(session_state, total_items, items_per_page, key='page'):
    """
    Incrementa a página atual no estado da sessão, se possível.
    """
    max_page = (total_items - 1) // items_per_page
    if session_state[key] < max_page:
        session_state[key] += 1


def prev_page(session_state, key='page'):
    """
    Decrementa a página atual no estado da sessão, se possível.
    """
    if session_state[key] > 0:
        session_state[key] -= 1
