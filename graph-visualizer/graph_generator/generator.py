from flask import current_app
from pyvis.network import Network
import networkx as nx
import os
import logging
from resources_inventory.inventory import k8s_supported_resources


class GraphGenerator():
    def __init__(self):
        self.net = None
        self.template_dir = f"{os.getcwd()}/templates/"
        self.view_name_resources = self.init_names_view()
        
    def init_names_view(self):
        result = {}
        for kv in k8s_supported_resources.items():
            result[kv[0].lower()] = kv[0]
        print(f"{result = }")
        current_app.logger.info(f"Initialized view names for resources: {result}")
        return result
    
    
    
    def generate(self, resource_name: str,templets_path:str,nx_graph:nx):

        


        # Here shold be an api call to the data-extraction service to get the data for the graph.
        # Request to [data-extraction-service]:/resources/<resource_name> 
        



        current_app.logger.info(f"Attenpting to create graph fro resource : {resource_name}")
        self.net = Network(notebook=True,height="1500px", width="100%", bgcolor="#222222", font_color="white")
        
        self.net.from_nx(nx_graph) # Convert networkx graph to pyvis Network 
        
        
        
        # statis_file_base_name = "network-graph-.html"
        # self.net.add_nodes(
        #     [id for id in range(1,11)],
        #     label=[ f"{self.view_name_resources.get(resource_name)}\n\n{id}" for id in (range(1,11))],
        #     color=["#00B8D4" for id in range(1,11)]
        # )
        # self.net.add_edge(1,2)
        # self.net.add_edge(1,3)
        # self.net.add_edge(7,4)
        # self.net.add_edge(4,5)
        # self.net.add_edge(3,6)
        # self.net.add_edge(3,7)
        # self.net.add_edge(3,8)
        # self.net.add_edge(5,9)
        # self.net.add_edge(5,10)        
        # self.net.get_node(1).update(color="#00BFA5")
        
        statis_file_base_name = "network-graph-.html"
        statis_file_name = statis_file_base_name.split('.')[0] + resource_name + "."+ statis_file_base_name.split('.')[1]
        statis_file_name = statis_file_name.split(".")[0] + ".html"
        full_path = f"{templets_path}/{statis_file_name}"
        logging.info(f"Generating graph with file name: {statis_file_name} , full path: {full_path}")
        try:
            self.net.show(full_path)
            current_app.logger.info(f"Created network graph at templates/{statis_file_name}.")
            return statis_file_name
        except Exception as e:
            logging.error(f"Error generating graph: {str(e)}")
        logging.info(f"Graph generated and saved at: {full_path}")