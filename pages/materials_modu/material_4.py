import streamlit as st
from utils.image_loader import get_image_path


#ページランクの導入、直径、平均経路長、成分数による崩壊の評価
#前回の続きからの実験

def intro():
    
    st.write("intro")

def chapter0():
    st.write("capter0")

def chapter1():
    st.write("capter1")

def chapter2():
    st.write("capter2")


def main_material():

    #ページ頭

    intro()
    
    st.divider()
    #サイドバー頭

    page=st.sidebar.radio("Chapter",["Chapter0","Chapter1","Chapter2"])
    
    if page == "Chapter0":
        chapter0()    
    
    elif page == "Chapter1":
        chapter1()
        
    elif page =="Chapter2":
        chapter2()