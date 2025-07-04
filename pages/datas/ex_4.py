import streamlit as st
from utils.image_loader import get_image_path
import streamlit.components.v1 as components




def ex_4():
    
    
    
    
    st.header("頑健性検証実験(7/4) Capter3")
    
    
    st.subheader("_1.random network(gilbert) model_",divider="violet")

    col1,col2=st.columns([1,1])
    html_path1=get_image_path("ex_4","G_RN_p001.html")
    html_path2=get_image_path("ex_4","G_RN_p002.html")
    html_path3=get_image_path("ex_4","G_RN_p003.html")
    html_path4=get_image_path("ex_4","G_RN_p004.html")
    html_path5=get_image_path("ex_4","G_RN_p010.html")
    with col1:
        with open(html_path1, "r", encoding="utf-8") as f:
            html1 = f.read()
        components.html(html1,height=500)
        with open(html_path3, "r", encoding="utf-8") as f:
            html3 = f.read()
        components.html(html3,height=500)
        with open(html_path5, "r", encoding="utf-8") as f:
            html5 = f.read()
        components.html(html5,height=500)        
    
    with col2:
        with open(html_path2, "r", encoding="utf-8") as f:
            html2 = f.read()
        components.html(html2,height=500)
        with open(html_path4, "r", encoding="utf-8") as f:
            html4 = f.read()
        components.html(html4,height=500)
        
    st.subheader("_2. watts-strogatz model_",divider="violet")
    col1,col2=st.columns([1,1])
    html_path1=get_image_path("ex_4","WS_K10p001.html")
    html_path2=get_image_path("ex_4","WS_K10p002.html")
    html_path3=get_image_path("ex_4","WS_K10p005.html")
    html_path4=get_image_path("ex_4","WS_K10p010.html")
    html_path5=get_image_path("ex_4","WS_K10p015.html")
    html_path6=get_image_path("ex_4","WS_K10p020.html")
    with col1:
        with open(html_path1, "r", encoding="utf-8") as f:
            html1 = f.read()
        components.html(html1,height=500)
        with open(html_path3, "r", encoding="utf-8") as f:
            html3 = f.read()
        components.html(html3,height=500)
        with open(html_path5, "r", encoding="utf-8") as f:
            html5 = f.read()
        components.html(html5,height=500)        
    
    with col2:
        with open(html_path2, "r", encoding="utf-8") as f:
            html2 = f.read()
        components.html(html2,height=500)
        with open(html_path4, "r", encoding="utf-8") as f:
            html4 = f.read()
        components.html(html4,height=500)
        with open(html_path6, "r", encoding="utf-8") as f:
            html6 = f.read()
        components.html(html6,height=500)    
    
    st.subheader("_3. Barabasi-albert model_",divider="violet")
    
    col1,col2=st.columns([1,1])
    html_path1=get_image_path("ex_4","BA_m1.html")
    html_path2=get_image_path("ex_4","BA_m2.html")
    html_path3=get_image_path("ex_4","BA_m3.html")
    html_path4=get_image_path("ex_4","BA_m5.html")
    html_path5=get_image_path("ex_4","BA_m10.html")
    with col1:
        with open(html_path1, "r", encoding="utf-8") as f:
            html1 = f.read()
        components.html(html1,height=500)
        with open(html_path3, "r", encoding="utf-8") as f:
            html3 = f.read()
        components.html(html3,height=500)
        with open(html_path5, "r", encoding="utf-8") as f:
            html5 = f.read()
        components.html(html5,height=500)        
    
    with col2:
        with open(html_path2, "r", encoding="utf-8") as f:
            html2 = f.read()
        components.html(html2,height=500)
        with open(html_path4, "r", encoding="utf-8") as f:
            html4 = f.read()
        components.html(html4,height=500)    

    st.subheader("_4-1. holme-kim model (p=0.3)_",divider="violet")    

    col1,col2=st.columns([1,1])
    html_path1=get_image_path("ex_4","HK_m1p030.html")
    html_path2=get_image_path("ex_4","HK_m2p030.html")
    html_path3=get_image_path("ex_4","HK_m3p030.html")
    html_path4=get_image_path("ex_4","HK_m5p030.html")
    with col1:
        with open(html_path1, "r", encoding="utf-8") as f:
            html1 = f.read()
        components.html(html1,height=500)
        with open(html_path3, "r", encoding="utf-8") as f:
            html3 = f.read()
        components.html(html3,height=500)
   
    
    with col2:
        with open(html_path2, "r", encoding="utf-8") as f:
            html2 = f.read()
        components.html(html2,height=500)
        with open(html_path4, "r", encoding="utf-8") as f:
            html4 = f.read()
        components.html(html4,height=500)    

    st.subheader("_4-2. holme-kim model (m=3)_",divider="violet")
    
    col1,col2=st.columns([1,1])
    html_path1=get_image_path("ex_4","HK_m3p001.html")
    html_path2=get_image_path("ex_4","HK_m3p002.html")
    html_path3=get_image_path("ex_4","HK_m3p005.html")
    html_path4=get_image_path("ex_4","HK_m3p050.html")
    with col1:
        with open(html_path1, "r", encoding="utf-8") as f:
            html1 = f.read()
        components.html(html1,height=500)
        with open(html_path3, "r", encoding="utf-8") as f:
            html3 = f.read()
        components.html(html3,height=500)
   
    
    with col2:
        with open(html_path2, "r", encoding="utf-8") as f:
            html2 = f.read()
        components.html(html2,height=500)
        with open(html_path4, "r", encoding="utf-8") as f:
            html4 = f.read()
        components.html(html4,height=500)   

