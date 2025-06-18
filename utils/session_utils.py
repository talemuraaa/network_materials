import streamlit as st

def is_initialized(key="initialized"):
    """一度だけ実行される初期化判定"""
    if key not in st.session_state:
        st.session_state[key] = True
        return False  # 初回
    return True


def clear_all_session_state():
    """すべての session_state を削除してリロード"""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()

    
def clear_session_keys(*keys):
    """指定されたキーのみ削除"""
    for key in keys:
        if key in st.session_state:
            del st.session_state[key]