from flask import current_app
from pyvis.network import Network
import networkx as nx
import os
import logging
from flask import current_app




def create_network_graph(number_of_nodes,current_route):
    statis_file_name = "network-graph.html"
    g = Network(notebook=True,
            cdn_resources="remote",
            height="1000px",
            width="100%",
            bgcolor="#222222", 
            font_color="white")
    # g = Network(notebook=True,
    #             cdn_resources="remote",
    #             height="750px",
    #             width="100%",
    #             select_menu=True,
    #             filter_menu=True,
    #             bgcolor="#222222", 
    #             font_color="white")
    nxg = nx.complete_graph(number_of_nodes)
    g.from_nx(nxg)
    g.show_buttons(filter_=['physics'])
    statis_file_name = statis_file_name.split(".")[0] + f"-{current_route}.html"
    full_path = f"{os.getcwd()}/templates/{statis_file_name}"
    print(f"{full_path =}")
    g.show(full_path)
    current_app.logger.info(f"Created network graph at templates/{statis_file_name}, with {number_of_nodes} nodes.")
    return statis_file_name


class GraphGenerator():
    def __init__(self,net:Network):
        self.net = net
        self.template_dir = f"{os.getcwd()}/templates/"
    
    def generate(self, file_name):
        full_path = f"{self.template_dir}{file_name}.html"
        logging.info(f"Generating graph with file name: {file_name}")
        try:
            self.net.show(full_path)
        except Exception as e:
            logging.error(f"Error generating graph: {str(e)}")
        logging.info(f"Graph generated and saved at: {full_path}")
        return full_path