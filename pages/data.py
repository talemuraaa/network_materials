import streamlit as st
from utils.image_loader import get_image_path
from utils import sideber_title

st.set_page_config(
    page_title="data"
    ,layout="wide"
)
sideber_title.sideber_title()

st.header("頑健性検証実験(6/20) Capter3")

st.write(" ”モデル名略称”(パラメータ),(ロバストネス指標R)")

st.subheader("_1.random network(gilbert) model_",divider="violet")

col1,col2=st.columns([1,1])
image_path1=get_image_path("targeted_attack(degree)_plot.png")
image_path2=get_image_path("targeted_attack(closeness)_plot.png")
image_path3=get_image_path("targeted_attack(eigenvector)_plot.png")
image_path4=get_image_path("targeted_attack(betweenness)_plot.png")
with col1:
    st.image(image_path1)
    st.image(image_path2)
with col2:
    st.image(image_path3)
    st.image(image_path4)

    
st.subheader("_2-1.watts-strogatz model_",divider="violet")
col1,col2=st.columns([1,1])
image_path1=get_image_path("targeted_attack(degree)_plot (1).png")
image_path2=get_image_path("targeted_attack(closeness)_plot (1).png")
image_path3=get_image_path("targeted_attack(eigenvector)_plot (1).png")
image_path4=get_image_path("targeted_attack(betweenness)_plot (1).png")
with col1:
    st.image(image_path1)
    st.image(image_path2)
with col2:
    st.image(image_path3)
    st.image(image_path4)
    
st.subheader("_2-2. watts-strogatz model(追加実験)_",divider="violet")
col1,col2=st.columns([1,1])
image_path2=get_image_path("targeted_attack(closeness)_plot (5).png")
image_path1=get_image_path("targeted_attack(closeness)_plot (6).png")
with col1:
    st.image(image_path1)
with col2:
    st.image(image_path2)

st.subheader("_3. Barabasi-albert model_",divider="violet")
col1,col2=st.columns([1,1])
image_path1=get_image_path("targeted_attack(degree)_plot (2).png")
image_path2=get_image_path("targeted_attack(closeness)_plot (2).png")
image_path3=get_image_path("targeted_attack(eigenvector)_plot (2).png")
image_path4=get_image_path("targeted_attack(betweenness)_plot (2).png")
with col1:
    st.image(image_path1)
    st.image(image_path2)
with col2:
    st.image(image_path3)
    st.image(image_path4)
    
st.subheader("_4-1. holme-kim model (m=3)_",divider="violet")
col1,col2=st.columns([1,1])
image_path1=get_image_path("targeted_attack(degree)_plot (3).png")
image_path2=get_image_path("targeted_attack(closeness)_plot (3).png")
image_path3=get_image_path("targeted_attack(eigenvector)_plot (3).png")
image_path4=get_image_path("targeted_attack(betweenness)_plot (3).png")
with col1:
    st.image(image_path1)
    st.image(image_path2)
with col2:
    st.image(image_path3)
    st.image(image_path4)
    
st.subheader("_4-2. holme-kim model (p=0.3)_",divider="violet")
col1,col2=st.columns([1,1])
image_path1=get_image_path("targeted_attack(degree)_plot (4).png")
image_path2=get_image_path("targeted_attack(closeness)_plot (4).png")
image_path3=get_image_path("targeted_attack(eigenvector)_plot (4).png")
image_path4=get_image_path("targeted_attack(betweenness)_plot (4).png")
with col1:
    st.image(image_path1)
    st.image(image_path2)
with col2:
    st.image(image_path3)
    st.image(image_path4)
    
    
