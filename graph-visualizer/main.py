from flask import Flask, render_template, request
from pyvis.network import Network
import networkx as nx
import os
from resources_inventory.inventory import k8s_supported_resources
from k8s_resources.resources import create_resources_bp


app = Flask(__name__)
templets_path = os.path.join(os.path.dirname(__file__), 'templates')

counter = 0

def delete_files_in_templates_directory():
    global counter 
    counter += 1
    # Delete all files inside the templates directory to force reerendering of the graph fro new requests.
    
    

    app.logger.info(f"Templets full path: {os.path.abspath(__file__)}")
    file_list = os.listdir(templets_path)
    
    for file in file_list:
        print(file)
    template_dir = templets_path
    for file_name in os.listdir(template_dir):
        file_path = os.path.join(template_dir, file_name)
        os.remove(file_path)
        

@app.after_request
def call_delete_files_in_templates_directory(response):
    delete_files_in_templates_directory()
    app.logger.info("Deleted all files in the templates directory.")
    return response

for resource in k8s_supported_resources.keys():
    app.register_blueprint(
        create_resources_bp(
            resource_type=resource,
            bp_name=resource,
            templets_path=templets_path
        ),
        url_prefix="/resources"
    )
    
@app.route("/endpoints")
def endpoints():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append(str(rule))
    return {"endpoints": routes}

