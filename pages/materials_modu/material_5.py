import streamlit as st
from utils.image_loader import get_image_path

def intro():
    st.write("""
             
         ## 第5回（7月25日）
         ### 0.直径の補足
         ### 1.頑健性検証実験

         """) 

def chapter0():
    st.header("_直径の計測方法について_")
    
    st.write("""
             前回、崩壊の評価指標の1つとして直径を導入した。        
             その際
             非連結なネットワークにおいても、ネットワーク全体の最大の最短経路長を直径として計算していた。     
             この方法では最大の直径をもつ成分以外の成分の直径は完全に無視されてしまう。
             
             ご指摘があったので、他の計算方法も考えてみることにした。
             
             
             #### ①全成分内で最大の直径をネットワーク全体の直径とする。 \n 
             
             #### ②各成分内の直径の平均をネットワーク全体の直径とする。\n
             
             #### ③各成分内の直径の加重平均をネットワーク全体の直径とする。\n
             
             ①は前回の計算方法と同様。②③はネットワーク全体の直径に複数の成分が影響を与えることができる。        
             ③の加重平均の重みは、各成分のサイズとする。
             
             このそれぞれの方法で実際に実験してみた。
             実装した関数は以下の通り。
             
             """)
    
    st.code("""
            
    import igraph as ig
            
    #方法１
    def max_diameters(G_ig:ig.Graph):
        return G_ig.diameter()

    #方法２
    def average_diameter(G_ig:ig.Graph):
        components=G_ig.components(mode="weak") #各連結成分のリストを作成
        diameters = [G_ig.subgraph(component).diameter() for component in components] #各連結成分の直径のリスト
        if len(diameters) == 0:
            return 0.0
        return sum(diameters) / len(diameters)

    #方法３
    def weighted_average_diameter(G_ig:ig.Graph):
        Components=G_ig.components(mode="weak") #各連結成分のリストを作成
        Diameters = [G_ig.subgraph(component).diameter() for component in Components] #各連結成分の直径のリスト
        weighted_sum=0
        total_nodes = 0
        for diameter,component in zip(Diameters,Components):
            size = len(component)
            weighted_sum += diameter*size
            total_nodes += size
        if len(Diameters) == 0:
            return 0.0
        return weighted_sum/total_nodes
            """,
            language="python")
    
    st.code("""
            
            def sum_diameter(G_ig:ig.Graph):
                return max_diameters(G_ig),average_diameter(G_ig),weighted_average_diameter(G_ig)
            
            
            def compare_with_dgree(G:nx.Graph):
    
                G_ig = ig.Graph.from_networkx(G)
                G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
                data_1,data_2,data_3=[compare_diameter(G_ig)[0]],[compare_diameter(G_ig)[1]],[compare_diameter(G_ig)[2]]
                while(G_ig.vcount() > 0):   
                    degree=G_ig.degree()
                    max_index = degree.index(max(degree))
                    G_ig.delete_vertices(max_index)                
                    data_1.append(compare_diameter(G_ig)[0])
                    data_2.append(compare_diameter(G_ig)[1])
                    data_3.append(compare_diameter(G_ig)[2])
                
                return data_1,data_2,data_3
            """)
    
    
    st.write("""
             この関数を用いて、複数の適当なモデルに対して実験を行う。なお、攻撃方法は標的型攻撃とする。\n
             実験結果は以下の通り。
             """)
    st.subheader("RNモデル（ギルバート） N=500,p=0.1")
    
    image_path=get_image_path("material_5","diameter_1.png")
    st.image(image_path)
    
    st.subheader("WSモデル N=500,k=5,p=0.3")

    image_path=get_image_path("material_5","diameter_2.png")
    st.image(image_path)

    st.subheader("BAモデル N=500,m=5")

    image_path=get_image_path("material_5","diameter_3.png")
    st.image(image_path)
    
    st.write("""
             - ３種のネットワークにおいて、②の直径は急激な増加はせず、緩やかに減少している。
             - 1つの成分の直径が飛びぬけて大きいだけで、それ以外のほとんどの成分の直径は極めて小さい？
             - ③は各成分の直径を加味した上で、①よりも細かく振動している。
             
             ③は①より優れた指標となり得る？
             
             （実装が間に合わなかったので、以降の実験は①のみをプロットしてます）
             """)
    
    

def chapter1():
    
    st.header("_頑健性検証実験_")
    
    st.write("""
             前回まではネットワークモデルを１つ定めて、そのパラメータを調整することでネットワークの頑健性にどのような影響があらわれるか
             を観察した。
             
             今回はネットワークのノード数と特徴量を１つ固定した異なるモデル間で頑健性を比較することにする。
             
             まずリンク数Lを固定する。ノード数Nも固定なので、おのずとリンク密度と平均次数が求まる。\n
             N=500,L=2500とすると、リンク密度d=0.02,平均次数<K>=10とわかる。
             この条件で実験を行う。
             
             今回はerdős-Rényランダムネットワークモデルを使用する。
             """)
    
    image_path1=get_image_path("ex_5","degree_1.png")
    image_path2=get_image_path("ex_5","closeness_1.png")
    image_path3=get_image_path("ex_5","betweenness_1.png")
    image_path4=get_image_path("ex_5","eigenvector_1.png")
    
    st.image(image_path1)
    st.image(image_path2)
    st.image(image_path3)
    st.image(image_path4)
    
    st.write("""
             - 結果から、ロバストネス指標Rの大きさは「ハブのあるネットワーク」＜「ハブのないネットワーク」とわかる。
             ハブは中心性が高く、狙い撃ちされやすいため妥当な結果と考えられる。
             - 同じ優先的選択のBAモデルとHMモデルの間には小さいが明らかな頑健性の差がある。     
             BAモデルにあって、HMにはない構造的特徴？用検討。
             
             """)
    
    st.write("""
             実験を通して、使用するネットワークモデルの数が少なく感じるので、３，４種類はモデルを追加したい。
             """)
    
    st.write("""
             
             """)
    
    st.subheader("夏季休暇やるかもリスト",divider=True)
    st.write("""
             以下のうち１つはやるかも
             
             - 崩壊のアニメーション制作
             - なにかしら(wikipedeiaとか)スクレイピングしてネットワーク解析とその可視化
             - dashアプリのデプロイ or デスクトップアプリ化
             """)

    
    st.subheader("来季の予定",divider=True)
    st.write("""
             
             - 頑健性実験続き
             - 新たなな崩壊度の指標の導入
             
             （以下はやりたいことリストだと思ってください。順不同）           

             - 次数相関
             - コミュニティ
             - 連鎖破綻のモデリングと実験
             - pagerankの導入
             - ボナチッチ・パワー中心性の導入
             - ペロン=フロベニウスの定理の証明
             
             """)


def main_material():

    #ページ頭

    intro()
    
    st.divider()
    #サイドバー頭

    page=st.sidebar.radio("Chapter",["0.直径の補足","1.頑健性検証"])
    
    if page == "0.直径の補足":
        chapter0()    
    
    elif page == "1.頑健性検証":
        chapter1()
