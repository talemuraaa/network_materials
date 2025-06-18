import streamlit as st
from pages.materials_modu import material_1,material_2

from utils import sideber_title

st.set_page_config(
    page_title="archive"
    ,layout="centered"
)


sideber_title.sideber_title()


st.markdown("# 📚発表資料アーカイブ")
st.divider()

page_id=st.sidebar.selectbox(
    '選択してください',
    ['第1回','第2回'])

if page_id == "第1回":
    material_1.main_material()
    
if page_id == "第2回":
    material_2.main_material()