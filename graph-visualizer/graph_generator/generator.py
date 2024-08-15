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
        return result
    
    
    
    def generate(self, resource_name: str,templets_path:str,nx_graph:nx):

        current_app.logger.info(f"Attenpting to create graph fro resource : {resource_name}")

        # self.net = Network(notebook=True,cdn_resources="in_line",bgcolor="#222222", font_color="white",filter_menu=True,height="1000", width="100%")
        self.net = Network(notebook=True,cdn_resources="in_line",bgcolor="#222222", font_color="white",height="1000", width="100%")
        
        self.net.from_nx(nx_graph) # Convert networkx graph to pyvis Network 
        
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