import os
import pandas as pd
import networkx as nx

def load_graph_from_csv(filename,names: tuple = ("node", "neighbors"),sep: str = ","):
    """
    CSVファイルからNetworkXのGraphオブジェクトを生成する。

    Parameters:
        filename (str): CSVファイル名（例: "sample.csv"）
        folder (str): CSVが保存されているフォルダ名（デフォルト: "csv_files"）

    Returns:
        networkx.Graph: 生成されたグラフ
    """
    this_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(this_dir,"..","csv_files", filename)
    df = pd.read_csv(path, header=None, dtype=str,names=names)
    G = nx.Graph()
    for _, row in df.iterrows():
            node = row["node"]
            # 空文字対策
            neigh_str = row["neighbors"]
            if pd.isna(neigh_str) or neigh_str == "":
                neighbors = []
            else:
                neighbors = [n.strip() for n in neigh_str.split(sep) if n.strip()]
            # ノード登録（孤立ノードを保持）
            G.add_node(node)
            # エッジ登録
            for nbr in neighbors:
                G.add_edge(node, nbr)
    return G