from pyvis.network import Network
import networkx as nx

G = nx.Graph()

G.add_nodes_from(["Politician_1","Politician_2","Politician_3"])
G.add_edges_from([("Politician_1","Politician_2"),("Politician_3","Politician_1")])


nt = Network('500px', '500px', notebook=True)

nt.from_nx(G)
nt.show('nx.html')