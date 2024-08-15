from flask import Blueprint, render_template, jsonify, request
from graph_generator.generator import GraphGenerator
from flask import current_app
from pyvis.network import Network
import networkx as nx
import os
from io import BytesIO
import requests





statis_file_base_name = "network-graph-.html"


def create_resources_bp(resource_type: str,bp_name,templets_path:str) -> Blueprint:
    k8s_resources_bp = Blueprint(bp_name,__name__)
     
    @k8s_resources_bp.route(f'/{resource_type.lower()}', methods=["GET"])
    def get_resource():

        
        current_app.logger.info(f"GET request received for {resource_type.lower()} resource")
        

        # 1. request resource graph (GML) data

        # 2. Load graph object (networkx)

        # 3. Create pyvis.network object from networkx

        # 4. Create graph page (UI- html)

        response = requests.get(f'http://localhost:8001/{resource_type.lower()}')
        networks_graph = None
        if response.status_code == 200:
            graphml_data = response.content  # Get the raw bytes from the response
        
            # Wrap the raw bytes in a BytesIO buffer
            graph_buffer = BytesIO(graphml_data)
            current_app.logger.info(f" Load graph buffer ")

            # Deserialize the graph from the buffer
            try:
                # Assuming you are receiving GML data, so use nx.read_gml
                gml_data = graph_buffer.getvalue().decode('utf-8')
                networks_graph = nx.parse_gml(gml_data)
                current_app.logger.info("Graph successfully deserialized from GML data.")
            except Exception as e:
                # Handle the exception, e.g., log the error
                current_app.logger.error(f"Failed to deserialize the graph: {e}")
            
        else:
            current_app.logger.error(f"Failed to retrieve graph data: {response.status_code}, {response.reason}")


        graph_generator = GraphGenerator()
        html_file_path = graph_generator.generate(resource_type.lower(),templets_path,networks_graph) 
        print(f"html file path {html_file_path}")
        return render_template(html_file_path)
        
    return k8s_resources_bp