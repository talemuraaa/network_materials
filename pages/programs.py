import streamlit as st

from utils import sideber_title,page_style

from module.experiments.main_hist import experiment_hist_ver2
from module.experiments import main_centrality,main_test,main_Vis


page_style.style("storage")

sideber_title.sideber_title()



main_pages=st.sidebar.selectbox("a",("Nerwrok model","Degree Distribution","Centrality"),label_visibility= "collapsed")

#ページ頭

st.title("🔨 ネットワーク保管庫")

if main_pages=="Nerwrok model":
    main_Vis.main_VIS_network()
    
elif main_pages=="Degree Distribution":
    experiment_hist_ver2()
    
elif main_pages=="Centrality":
    main_centrality.main_centrality()
    
elif main_pages=="test":
    main_test.plot_3d()
