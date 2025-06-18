import streamlit as st
from utils import sideber_title,page_style,session_utils
from module.experiments import main_attack_net


page_style.style("attack")


sideber_title.sideber_title()
st.title("🏹Attack on network")

main_page=st.sidebar.selectbox("選択してください",("1","2"),label_visibility="collapsed")

if main_page=="1":
    graph_keys = [key for key in st.session_state.keys() if key.endswith("_graph")]
    st.write(graph_keys)
    session_utils.clear_session_keys(graph_keys)
    main_attack_net.multi_attack_to_network()
if main_page=="2":
    graph_keys = [key for key in st.session_state.keys() if key.endswith("_graph")]   
    st.write(graph_keys) 
    session_utils.clear_session_keys(graph_keys)
    main_attack_net.single_attack_to_muluti_network()
