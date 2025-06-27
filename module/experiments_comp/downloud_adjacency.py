import pandas as pd
import streamlit as st
import networkx as nx
from io import StringIO


def downloud_adjacency_list_button(G:nx.Graph, filename: str = "adjlist.csv", key: str = "download"):
    rows = []
    for u in G.nodes():
            neighbors = sorted(G.neighbors(u))
            neighbor_str = ",".join(map(str, neighbors))
            rows.append({"node": u, "neighbors": neighbor_str})

    
    df = pd.DataFrame(rows)
    
    csv_buffer = StringIO()
    df.to_csv(csv_buffer,index=False,header=False)
    csv_data=csv_buffer.getvalue()
    
    st.download_button(
        label="download",
        data=csv_data,
        file_name=filename,
        mime="text/csv",
        type='primary',
        key=key
        )


#adj_list=nx.to_pandas_edgelist(G)

#adj_list={node: list(G.adj[node])for node in G.nodes}
#df = pd.DataFrame([(k, v) for k, vs in adj_list.items() for v in vs])