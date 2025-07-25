import streamlit as st
from utils import sideber_title,page_style
from pages.materials_modu import material_5


page_style.style("materials")

st.title("📖発表資料")
st.divider()

sideber_title.sideber_title()

material_5.main_material()
