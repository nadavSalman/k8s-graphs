from pyvis.network import Network
import networkx as nx



pod_img_address = "https://github.com/kubernetes/community/raw/master/icons/png/resources/unlabeled/pod-128.png"

net = Network(bgcolor="#222222",font_color="white")


net.add_node(1, label="pod_1", image=pod_img_address, shape="image")
net.add_node(2, label="pod_2", image=pod_img_address, shape="image")
net.add_node(3, label="pod_3", image=pod_img_address, shape="image")


net.add_edge(1, 2)
net.add_edge(1, 3)





# net.add_nodes(
#     [id for id in range(1, 101)],
#     label=[f"pod_{id}" for id in range(1, 101)],
#     image=[pod_img_address for id in range(1, 101)],
#     shape=["image" for id in range(1, 101)],
#     # color=["#00E5FF" for id in range(1, 101)]
# )

# net.add_edges([(1, 2), (1, 3)])
# net.add_edges([(2, 4), (2, 5), (3, 6), (3, 7)])
# net.add_edges([(6, 8), (6, 9), (6, 10)])

# for i in range(1, 11):
#     net.add_edges([(i, i + 10), (i, i + 20)])
#     net.add_edges([(i + 10, i + 30), (i + 10, i + 40)])
#     net.add_edges([(i + 20, i + 50), (i + 20, i + 60)])

net.show("test.html")