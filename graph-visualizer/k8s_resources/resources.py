from flask import Blueprint, render_template, jsonify, request
from resources_inventory.incentory import k8s_supported_resources
from flask import current_app
from pyvis.network import Network
import networkx as nx
import os




statis_file_base_name = "network-graph-.html"


def create_resource_graph(resource_name: str):
    
    ## Generate Graph form GraphGenerator
    
    
    
    
    net = Network(notebook=True)
    net.add_nodes(
        [id for id in range(1,11)],
        label=[ f"pod_{id}" for id in (range(1,11))],
        color=["#00E5FF" for id in range(1,11)]
    )
    
    for i in range(2,11):
        net.add_edge(i,1)
    net.add_edge(7,2)
    net.add_edge(7,10)
    net.add_edge(7,3)
        
    

    statis_file_name = statis_file_base_name.split('.')[0] + resource_name + "."+ statis_file_base_name.split('.')[1]
    # full_path = f"{os.path.dirname(os.getcwd())}/templates/{statis_file_name}"
    print(f" os.getcwd() -> {os.getcwd() }")
    full_path = f"{os.getcwd()}/templates/{statis_file_name}"
    

    statis_file_name = statis_file_name.split(".")[0] + f"-{10}.html"
    full_path = f"{os.getcwd()}/templates/{statis_file_name}"
    print(f"{full_path =}")
    # g.show(full_path)
    
    net.show(full_path)
    current_app.logger.info(f"Created network graph at templates/{statis_file_name}.")
    return statis_file_name
    
    

def create_deployment_graph():
    pass


def create_resources_bp(resource_type: str,bp_name) -> Blueprint:
    k8s_resources_bp = Blueprint(bp_name,__name__)
     
    @k8s_resources_bp.route(f'/{resource_type.lower()}', methods=["GET"])
    def get_resource():
        current_app.logger.info(f"GET request received for {resource_type} resource")
        html_file_path = create_resource_graph(resource_type.lower())
        print(f"html file path {html_file_path}")
        # current_app.logger.info(f"{create_resource_graph(resource_type.lower()) = }")
        return render_template(html_file_path)
        # return jsonify({resource_type : k8s_supported_resources.get(resource_type)}), 200
        
    return k8s_resources_bp