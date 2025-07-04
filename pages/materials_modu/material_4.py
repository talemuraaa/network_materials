import streamlit as st
from utils.image_loader import get_image_path
import streamlit.components.v1 as components



#ページランクの導入、直径、平均経路長、成分数による崩壊の評価
#前回の続きからの実験

def intro():
    st.write("""
             
         ## 第4回（7月?日）
         ### 0.いろいろ
         ### 1.直径による崩壊の評価
         ### 2.頑健性検証実験
         """) 

def chapter0():
    
    st.subheader("dashについて")
    st.write("""
             前回のとおりdashでアプリを制作中です。ので、streamlitの方で新しい機能はないです。
             """)
    st.write("""
             plotlyで生成するグラフは調整中。細かい設定が大量にあって主要なものしか実装できていないです。
             実験パートで改めて紹介しますが、以下のようなグラフをplotly(dash内)で出力及びダウンロードできるようにしました。  
             """)

    html_pass=get_image_path("ex_4","G_RN_p004.html")
    
    with open(html_pass, "r", encoding="utf-8") as f:
        html = f.read()
    components.html(html,height=600)
    
    st.subheader("networkx計算遅すぎ問題")
    
    st.write("""
             _networkx_ の中心性の計算にはとんでもなく時間がかかります。
             特に媒介中心性の計算が果てしなく長いです。
             """)
    
    st.code("""
            import networkx as nx
            
            nx.degree_centrality(G,node) #次数中心性
            nx.closeness_centrality(G,node) #近接中心性
            nx.eigenvector_centrality(G.node) #固有ベクトル中心性
            nx.betweenness_centrality(G.node) #媒介中心性
            
            #返り値は辞書型
            """,language="python")
    
    st.write("大規模なネットワークを解析するには使いづらい…")
    
    st.subheader("_igraph_")
    st.write("""
             netwrokx以外に代表的なグラフに特化したライブラリとしてigraphがあります。
             igraphはc言語ベースのライブラリのため、pythonベースのnetworkxよりも非常に高速。
             上位互換とかではないです。
             
             あくまでも処理速度が足りないと感じている部分（今回は中心性の計算）のみに補助的に利用。メインはnetworkx。
             以下のようにしてnetworkxのグラフオブジェクトをigraphのグラフオブジェクトに変換可能です。
             """)
    
    
    
    st.code("""
            import igraph as ig

            G_ig = ig.Graph.from_networkx(G)

            """,language="python")
    
    st.write(""" 
             ノードにラベルを明示的に書き込み。     
             ノードの追加、削除などを行わないのであれば必要ないかも？
             """)
    
    st.code("""
            G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
            """,language="python")
    
    st.write("実際にプログラムにigrphを組み込んだ例")
    
    st.code("""
            def degree_traget_attack(G:nx.graph):

                N=nx.number_of_nodes(G)
                G_ig = ig.Graph.from_networkx(G)
                G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
                dta = [len(max(nx.connected_components(G), key=len, default=[]))/N] #初期状態のSをリストに追加
                while(G_ig.vcount() > 0):   
                    degrees=G_ig.degree() #全ノードの次数（中心性）をlistに格納
                    max_index = degrees.index(max(degrees)) #最大次数のindex(label)を取得
                    G_ig.delete_vertices(max_index)         #lndexに従いノードを除去
                    maxcom=G_ig.components(mode="weak").giant() 
                    dta.append(maxcom.vcount()/N)   #崩壊後のSをリストに追加
                
                return dta
            """)
    
    st.caption("次数中心性に基づく標的型攻撃を行い、その結果をリストに格納する関数。")
    
    st.write("""
             ノード数1000ぐらいのネットワークに対して、処理速度は数十倍になった気がします。       
             計測してないので気がするだけです。
             """)

def chapter1():
    
    st.header("_直径_")
    

    st.write("""
                 ネットワークの直径（diameter）は、すべてのノードのペアにおける最短経路長の最大値、すなわち最長の最短経路である。 
                 """)

    with st.container(border=True):
        st.subheader("直径 $l_{max}$",divider=  "gray")
        

        
        st.latex(r'''
                 
            l_{max}=\underset{ij}{max} \, {l_{ij}} 
            
            ''')
        
        st.write("""
                 ${l_{ij}}$:ノード$i$とノード$j$の距離
                 """)

    st.write("""
            この直径を用いて、ネットワークの崩壊を観察する。
            直径が大きくなるということは、ネットワーク全体の
                 """)

def chapter2():
    st.write("""
             前回と同じ形式（１つの戦略にパラメータを変えた複数のネットワーク）を作るつもりが、
             1つのネットワークに対して複数の戦略になってしまいました。。。
             
             すべて並べてあるので比較自体はできるけど、やりづらくなってます。。。
             
             現時点ではmatplotlibで生成したものの方が見やすいですが、次回までにはもう少し改善させます。
             
             直径を加えたネットワークの頑健性検証実験は「実験データ保管個」へ。
             """)
    st.subheader("次回以降の予定",divider=True)
    st.write("""
             
             - 頑健性実験の続き
             
             （以下はやりたいことリストだと思ってください。順不同）           

             - 次数相関
             - コミュニティ             
             - パーコレーション概要　→　モロイ・リード基準とその導出　→　臨界しきい値の導出
             - 連鎖破綻のモデリングと実験
             - ボナチッチ・パワー中心性の導入
             - ペロン=フロベニウスの定理の証明
             - なにかしら(wikipedeiaとか)スクレイピングしてネットワーク解析


             """)


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