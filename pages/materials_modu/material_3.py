import streamlit as st
import pandas as pd
from utils.image_loader import get_image_path
from csv_files.csv_loader import load_graph_from_csv
from module.experiments_comp.draw_plot import draw_2Dplot_go,draw_3Dplot_go


def intro():
    st.write("""
             
         ## 第3回（6月?日）
         ### 0.いろいろ
         ### 1.固有ベクトル中心性
         ### 2.頑健性実験
         """)    
    
def chapter0():
    
    st.subheader("崩壊度$s$について")
    
    with st.container(border=True):
        
        st.subheader("$崩壊度S$",divider="violet")
        st.write("ネットワークの崩壊度を、ネットワークの最大連結成分と攻撃前のネットワークのサイズの割合$S$として定義する。 ")
        st.latex(r'''
                
                S=\frac{C_{max}}{N} 
                
                ''')
        
        st.write("""
                
                $C_{max}$ : 最大連結成分のサイズ  
                $N$ : 初期状態のネットワークのサイズ
                
                """)    
    
    st.write("""
             前回は上のように定義した。
             
             読み返して感じたが、「崩壊度」という名前が不適各な気がする。
             
            「崩壊度」は、、便宜上「崩壊度」と勝手に命名しただけ。
            崩壊度が高い（１に近い）ほどネットワークの最大連結成分が大きい、つまり、崩壊していない。名前と直観が反している気がする。
            
            抵抗度？
            か
            残存度？
            か
            「初期状態のサイズに対する最大連結成分の割合」？
            
             """)
        

    st.subheader("plotlyのあれこれ")
    
    st.write("""
             
             前回紹介したplotlyが思ったより面白い。インタラクティブなグラフや、3Dのオブジェクトを作るのが結構楽しい。
             公式のリンクはhome。
             
             plotlyが、一般的な可視化ライブラリのmatplotlibと大きくことなる点の1つが、インタラクティブなグラフを生成できること。
             ネットワークを描画した際、カーソルを合わせることで、そのノードのラベルや特徴量を表示することができる。
             
             ただコードはmatplotlibと比べて何倍も長くなるので、すこし面倒。 
             """)
    
    st.write("""
             ただこんなこともできる。
             以下は同じネットワークを２次元と３次元で可視化した例。もちろん細かい調整もできる。
             """)
    
    
    
    G=load_graph_from_csv("adjlist_1.csv")
    fig2=draw_2Dplot_go(G,node_size=10)
    
    st.plotly_chart(fig2)
    fig3=draw_3Dplot_go(G,node_size=6)
    st.plotly_chart(fig3)
    
    st.write("""
             このようにインタラクティブで拡張性が非常に高い。
             
             ただ、静止画と比べてファイルサイズは大きく、オブジェクトが大きく
             なると動作も重くなる点には注意が必要。
             
             ２次元でも３次元の場合でも、結局はノードやリンクのフィルタリングが必要になる。
             """)
    
    st.subheader("_Dash_")
    
    st.write("""
             
             調べてみると、plotlyと相性のいい「Dash」というフレームワークがあるらしい。
             https://dash.plotly.com/
             
             それとは別に、いろいろな機能を実装していたらstreamlitの読み込みがどんどん重くなり、
             streamlitの限界をひしひしと感じている。
             
             ということでstreamlitでのアプリ開発は今回まで！！
             
             ひとまず次回以降からは、dashでアプリを開発しつつ、streamlitの機能を移植！！
             
             今後、streaamlitは発表資料やプログラム置き場とする方針で行きたい。
              """)

def chapter1():
    st.header("固有ベクトル中心性")
    st.write("""
             前回、３種類の中心性の定義を確認した。
             それぞれ何を重要とするかによって別々の定義がなされている。
             
             ここでは「誰に接続しているか」に着目した中心性を考えることにする。
             
             たとえば、政治家において、その人脈の豊かさでその人の評判が決まることは自然である。
             より有力な政治家とつながれば、その人の評判も高くなる。
             
             
             
             """)
    
    st.write("""
             まず各ノード$i$の中心性を$c_{i}$として、それらをベクトルとして
             """)
    
    st.latex(r'''
             
             c=
             
             \begin{pmatrix}
            c_1  \\
            \vdots \\
            c_i  \\
            \vdots \\
            c_n  \\    
            \end{pmatrix}
             ''')
    
    st.write("""を考える。また与えられたネットワークの隣接行列を""")
    
    
    st.latex(r'''
             
             G=
            \begin{pmatrix}
            g_{11}  & g_{12}  & \cdots  & g_{1n}\\
            g_{21}  & g_{22} & \cdots & g_{2n}\\
            \vdots & \ddots & & \vdots \\
            \vdots & & \ddots & \vdots \\             
            g_{n1}  & \cdots & \cdots & g_{nn}\\    
            \end{pmatrix} 
             ''')
    
    st.write("""
             とする。
             
            このとき、
             """)
    
    st.latex(r'''
             
             Gc=
             
             \begin{pmatrix}
            g_{11}c_{1} + g_{12}c_{2}  & \cdots & g_{1n}c_{n} \\
            \vdots \\
            g_{i1}c_{1} + g_{i2}c_{2}  & \cdots & g_{in}c_{n} \\
            \vdots \\
            g_{n1}c_{1} + g_{n2}c_{2}  & \cdots & g_{nn}c_{n} \\  
            \end{pmatrix}
             
             =
             
              \begin{pmatrix}
            \sum_{j=1}^{n} g_{1j} c_{j}  \\
                
            \vdots \\
            \sum_{j=1}^{n} g_{ij} c_{j}  \\

            \vdots \\
            \sum_{j=1}^{n} g_{nj} c_{j} 
            \end{pmatrix}
             
             
             ''')
    
    st.write("""
             この時、$G$は隣接行列なので $g_{ii}=0$
             
             ノード$k$について、ノード$i$と隣接している場合$g_{ki}=1$、していない場合$g_{ki}=0$
             
             つまり$\sum_{j=1}^{n} g_{ij} c_{j}$ はノード$i$の隣接ノード$j$の中心性の総和になる。
             
             このことからノードiの中心性は以下のように表すことができる。
             """)
    
    st.latex(r"""
             
             c_{i}
             
             =
             
             \sum_{j=1}^{n} g_{ij} c_{j}
             
             """)
    
    st.write("""
             これはまさに「誰に接続しているか」に着目した中心性になっている。
             
             しかしこの中心性を定義するためには
             """)
    
    st.latex(r"c=Gc")
    
    st.write("""
             とならなければならない。
             
             また、あるノードAの中心性を計算するのに、その隣接ノードの中心性が必要だが、その隣接ノードの中心性を
             計算するにはノードAの中心性が必要になる。
             
             ひとまずを$c=Gc$満たす$c$、$G$について考えることにする。
             
             突然だが、ここで隣接行列$G$の固有値、固有ベクトルについて考えてみる。

             $G$の固有値$\lambda$、固有ベクトル$c$が求まったとして、
             """)

    st.latex(r"""
             
             
             Gc=\lambda c
            \\
            　
            \\
             c =\frac{1}{\lambda} G c
             
             """)
    
    st.write("""
             と表せる。（対称行列なので固有値は実数）
             
             しかし、固有値は必ず１つに定まるわけではない。
             さらに固有ベクトルの成分が負になることも考えられる。
             つまりマイナスの中心性が現れてしまうことになる。
             """) 
    
    with st.container(border=True):
        st.subheader("ペロン=フロベニウスの定理（？）",divider=  "gray")
        
        st.write("""
                 非負行列$A$は次のような固有値$a$を持つ。
                 - 任意のAの固有値$\lambda$に対して、$|\lambda| < |a| $
                 - aに対する非負の固有ベクトルが存在し、a以外の固有値に対する非負の固有ベクトルは存在しない
                 
                 """)
        
    st.write("""
             任意の隣接行列は非負行列であるため、ペロン=フロベニウスの定理からＧの絶対値が最大の固有値に
             着目すると、対応する固有ベクトルで成分がすべて非負のものが得られる。
             
             このようにすると、中心性が負となるとなる問題を避けるだけではなく、計算に用いる固有値を１つに定めることができる。
             """)
    
    
    
    with st.container(border=True):
        st.subheader("固有ベクトル中心性$c_i$",divider=  "gray")
        
        st.latex(r'''
             c_i =\frac{1}{\lambda} \sum_{j=1}^{n} g_{ij} c_{j}
            ''')
        
        st.write("ただし、Gの固有値の中で絶対値が最大のものを$\lambda$、それに対応する固有ベクトルを$c$とする。")
        
    st.divider()
    
    st.subheader(" _ぺロン=フロベニウスの定理 証明_")
    
def chapter2():
    st.header("頑健性実験")
    st.write("""chapter2""")

    
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