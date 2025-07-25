import streamlit as st

from utils import sideber_title
from pages.datas import ex_3,ex_4,ex_5

st.set_page_config(
    page_title="data"
    ,layout="wide"
)
sideber_title.sideber_title()

page=st.sidebar.selectbox(
    '選択してください',
    ['第3回','第4回','第5回'])

if page=='第3回':
    ex_3.ex_3()
    
elif page=='第4回':
    ex_4.ex_4()

elif page=='第5回':
    ex_5.ex_5()


    
    
