import networkx as nx 
import random as rd
import igraph as ig


def random_failure(G:nx.graph):
    
    N=nx.number_of_nodes(G)
    node_list = list(G.nodes)
    rf = [len(max(nx.connected_components(G), key=len, default=[]))/N]
    rd.shuffle(node_list)
    for i in node_list:
        G.remove_node(i)
        maxcom = len(max(nx.connected_components(G), key=len, default=[]))
        rf.append(maxcom / N)

    return rf

def degree_traget_attack(G:nx.graph):

    N=nx.number_of_nodes(G)
    G_ig = ig.Graph.from_networkx(G)
    G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
    dta = [len(max(nx.connected_components(G), key=len, default=[]))/N]
    while(G_ig.vcount() > 0):   
        betweenness=G_ig.degree()
        max_index = betweenness.index(max(betweenness))
        G_ig.delete_vertices(max_index)                
        maxcom=G_ig.components(mode="weak").giant()
        dta.append(maxcom.vcount()/N)
    
    return dta

def closeness_traget_attack(G:nx.graph):
    N=nx.number_of_nodes(G)
    G_ig = ig.Graph.from_networkx(G)
    G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
    cta = [len(max(nx.connected_components(G), key=len, default=[]))/N]
    while(G_ig.vcount() > 0):
        
        closeness=G_ig.harmonic_centrality()
        max_index = closeness.index(max(closeness))
        G_ig.delete_vertices(max_index)      
        maxcom=G_ig.components(mode="weak").giant()
        cta.append(maxcom.vcount()/N)
        
    return cta

def betweenness_target_attack(G:nx.graph):

    N=nx.number_of_nodes(G)
    G_ig = ig.Graph.from_networkx(G)
    G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
    bta = [len(max(nx.connected_components(G), key=len, default=[]))/N]
    while(G_ig.vcount() > 0):
        
        betweenness=G_ig.betweenness()
        max_index = betweenness.index(max(betweenness))
        G_ig.delete_vertices(max_index)                
        maxcom=G_ig.components(mode="weak").giant()
        bta.append(maxcom.vcount()/N)

    return bta

def eigenvector_target_attack(G:nx.graph):

    N=nx.number_of_nodes(G)
    G_ig = ig.Graph.from_networkx(G)
    G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
    eta = [len(max(nx.connected_components(G), key=len, default=[]))/N]
    while(G_ig.vcount() > 0):
        
        eigenvector=G_ig.eigenvector_centrality()
        max_index = eigenvector.index(max(eigenvector))
        G_ig.delete_vertices(max_index)                
        maxcom=G_ig.components(mode="weak").giant()
        eta.append(maxcom.vcount()/N)

    return eta
