import streamlit as st
from utils import sideber_title

#streamlit run app.py

st.set_page_config(
    page_title="HOME"
    ,layout="centered"
)

sideber_title.sideber_title()

st.title(" _HOME_ 🏠")
st.write("""
          - 発表資料:本日の発表資料
          - ネットワーク保管庫:使用したネットワーク、その可視化、使用したプログラムなど随時追加。
          - アーカイブ: 過去の発表資料を公開。2回目以降から随時追加予定。
         """)

st.divider()



st.header("参考サイト")

st.markdown("""
            
            - #### plotly-networkxの描画        
            https://plotly.com/python/network-graphs/
    
            - #### plotly-3D描画
            https://plotly.com/python/v3/3d-network-graph/
            
            - #### _Enhancing structural robustness of scale-free networks by information disturbance_
            https://www.nature.com/articles/s41598-017-07878-2
            """)


st.header("参考書籍")

st.markdown(
        """
        #### 1. _ネットワーク科学入門_ 
        https://www.maruzen-publishing.co.jp/book/b10123080.html
        #### 2. _ゲーム理論からの社会ネットワーク分析_  
        https://www.ohmsha.co.jp/book/9784274230899/
        #### 3. __ネットワーク科学__ 
        https://www.kyoritsu-pub.co.jp/book/b10003149.html 
        #### 4. __複雑ネットワークにおける最適化__ 
        https://www.kindaikagaku.co.jp/book_list/
        https://www.kyoritsu-pub.co.jp/book/b10003845.html

        """
    )




