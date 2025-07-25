import networkx as nx
import random as rd
import math
from collections import Counter

#自作モデル集

def random_walk_graph(N,m,p):
    G=nx.complete_graph(4)
    for i in range(4,N):   
        l=list(nx.nodes(G))
        j=rd.choice(l)
        G.add_edge(i,j)
        
        selected=set([i])
        
        for _ in range(m-1):
            random_value = rd.random()
            #確率ｐで隣接ノードに接続するかしないか場合分け。
            if random_value<p:
                
                #ｎからランダムに一つノードｓを選択。
                #リンクｉｓを生成。
                
                unvisited_neighbors = [n for n in G.neighbors(j) if (n not in selected )]
                
                if not unvisited_neighbors:
                    break
                
                s=rd.choice(unvisited_neighbors)
                G.add_edge(i,s)
                selected.add(s)
              
            else:

                #リストからランダムにノードｓを選択。リンクｉｓを生成。
                unvisited_nodes = [n for n in G.nodes if (n not in selected)]
                if not unvisited_nodes:
                    break
                s=rd.choice(unvisited_nodes)  
                G.add_edge(i,s)
                selected.add(s)
           
    return G

def step_RW_graph(N,p,l=None):
    
    if not l:
        l=N
    
    G=nx.complete_graph(4)
    #初期状態N＝４の完全グラフ
    for i in range(4,N):
        #ノードリストｌを取得。
        #ノードiを追加、ノードリストｌからランダムに一つノードｊを選択。
        #リンクｉｊを生成。
        node_list=list(nx.nodes(G))
        j=rd.choice(node_list)
        G.add_edge(i,j)
        
        #ノードｊの隣接ノードリストｎを取得。
                
        #乱数を生成。
        
        random_value = rd.random()
        
        #確率ｐで隣接ノードに接続するかしないか場合分け。
        
        if random_value<p:
            #到達済み判定
            #ウォークを格納
            current_node=j
            walk=[current_node]
            visited = set(walk)
            for _ in range(l):
                if rd.random()<p:
                    unvisited_neighbors = [n for n in G.neighbors(current_node) if (n not in visited and n!=i)]
                    if unvisited_neighbors:
                        next_node = rd.choice(unvisited_neighbors)
                        walk.append(next_node)
                        visited.add(next_node)
                        current_node = next_node
                    else :
                        #移動先無しで終了
                        break
                else:
                    #1-pで終了
                    break
            
            for k in walk:
                G.add_edge(i,k)    
            
    
        else: 
            node_list.remove(j)
            s=rd.choice(node_list)
            G.add_edge(i,s)
            
    return G

#次数に基づき山登りを行い、その軌跡とリンクを接続

def mauntein_graph(N:int):
    G=nx.complete_graph(4)

    for i in range(4,N):
        node_list=list(nx.nodes(G))
        j=rd.choice(node_list)
        
        current_node=j
        path=[current_node]
        neighbor_list=nx.neighbor_degree(j)
        
        #隣接ノードの中で最も次数の高いノードに移動。自分より次数が高いノードがない場合は移動しない。
        while(nx.degree(current_node) > neighbor_list):
            next_node=max(neighbor_list)
            neighbor_list=nx.neighbor_degree(next_node)
            path.append(next_node)
            current_node=next_node
        for k in path:
            G.add_edge(i,k)   
        
    return G


def ex_cluster_graph(N:int,p:float,x:int,A=2.0)->nx.Graph:
    """
    ・return :Graph\n
    ・動的なネットワーク生成モデル。\n
    ・ノード追加の際、ランダムな一点を選び、そこからl回ランダムウォークを行う。
    この時、確率pでランダムジャンプを行う。到達回数がx以上のノードのみとリンクを接続する。\n
    ・ネットワークサイズに応じて、探索範囲を対数スケールで拡大\n
    ・initial_nodesの大きさは仮
    """
    
    initial_nodes = int(3 * math.log(N))
    G=nx.complete_graph(initial_nodes)
    
    for i in range(initial_nodes,N):
        l = math.ceil(A * math.log(max(2, i)))
        
        node_list=list(nx.nodes(G))#ノードリストを取得。
        j=rd.choice(node_list)
        
        visited_count = Counter()#到達回数をカウント
            
            
        current_node=j#現在位置
            
        for _ in range(l): #ノードjからランダムウォークを開始
            if rd.random()<1-p: #確率1-pで隣接ノードに移動
                neighbors = list(G.neighbors(current_node))#jの隣接ノードのリスト
                if neighbors:
                    next_node = rd.choice(neighbors)#リストからランダムに１つnext_nodeを選択
                    visited_count[next_node] += 1 #到達回数カウント＋１
                    current_node = next_node
            else: #確率pでランダムなノードにテレポート
                next_nodes=[node for node in G.nodes() if node != current_node]
                next_node=rd.choice(next_nodes)
                visited_count[next_node] += 1 #到達回数カウント＋１
            
        add_link_list= [node for node, count in visited_count.items() if count >= x]
        
        for node in add_link_list:
            G.add_edge(i,node)
                
    return G
        
        

        
        