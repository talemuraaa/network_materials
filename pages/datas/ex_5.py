import streamlit as st
from utils.image_loader import get_image_path

def ex_5():
    
    st.header("頑健性検証実験(7/24) Capter3")
    
    st.subheader("_1.L=2500_",divider="violet")
    col1,col2=st.columns([1,1])
    image_path1=get_image_path("ex_5","degree_1.png")
    image_path2=get_image_path("ex_5","closeness_1.png")
    image_path3=get_image_path("ex_5","betweenness_1.png")
    image_path4=get_image_path("ex_5","eigenvector_1.png")
    
    with col1:
        st.image(image_path1)
        st.image(image_path2)
    with col2:
        st.image(image_path3)
        st.image(image_path4)
        
    st.subheader("_1.L=3000_",divider="violet")
    col1,col2=st.columns([1,1])
    image_path1=get_image_path("ex_5","degree_2.png")
    image_path2=get_image_path("ex_5","closeness_2.png")
    image_path3=get_image_path("ex_5","betweenness_2.png")
    image_path4=get_image_path("ex_5","eigenvector_2.png")
    
    with col1:
        st.image(image_path1)
        st.image(image_path2)
    with col2:
        st.image(image_path3)
        st.image(image_path4)