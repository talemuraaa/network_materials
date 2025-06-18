import streamlit as st
from utils import sideber_title
from pages.materials_modu import material_3

st.set_page_config(
    page_title="archive"
    ,layout="centered"
)


st.title("📖発表資料")
st.divider()

sideber_title.sideber_title()

material_3.main_material()
