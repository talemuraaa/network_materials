import streamlit as st

def style(title):
    
    st.set_page_config(
        page_title=f"{title}"
        ,layout="wide"
    )
    
    st.markdown(""" 
        <style> 
        [data-testid="stVerticalBlock"] {
            max-width: 900px;
            margin: 0 auto;
            padding: 0rem;
        }
        </style>
    """, unsafe_allow_html=True)
    