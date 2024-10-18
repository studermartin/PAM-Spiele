import networkx as nx

# https://networkx.org/documentation/stable/reference/algorithms/dag.html
dg = nx.DiGraph()
dg.add_node("R")
dg.add_node("R.1")
dg.add_node("R.1.1")
dg.add_node("R.1.2")
dg.add_edge("R", "R.1")
dg.add_edge("R.1", "R.1.1")
dg.add_edge("R.1", "R.1.2")

# Pretty printing
# https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.text.write_network_text.html
nx.write_network_text(dg)

# Postorder traversal
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.traversal.depth_first_search.dfs_postorder_nodes.html
print(list(nx.dfs_postorder_nodes(dg, source="R")))
for node in dg.nodes:
    if dg.out_degree(node)==0:
        print(node)

