from flask import Blueprint, jsonify, Response
from flask import current_app
from graph_data_extraction.data_extraction import K8sResourcesDataExtraction
from kubernetes import client, config
from io import BytesIO
import networkx as nx



def create_resources_bp(resource_type: str,k8s_client: client.CoreV1Api) -> Blueprint:
    k8s_resources_bp = Blueprint(resource_type,__name__)
    k8s_exctractor = K8sResourcesDataExtraction()
     
    @k8s_resources_bp.route(f'/{resource_type.lower()}', methods=["GET"])
    def get_resource():
        current_app.logger.info(f"GET request received for {resource_type} resource")

        # extracted data towill hold graph object
        # Dynamic function call
        nx_graph = k8s_exctractor.solve_for(
            name = f'extracted_{resource_type}s_data',
            k8s_client=k8s_client)
        

        # Serialize Options : 

        # Serialize the graph to GML (GraphML) format
        output = BytesIO()
        nx.write_gml(nx_graph, output)
        graphml_data = output.getvalue()

        # Create a response with the GraphML data
        # The mimetype parameter tells the client what type of content is being sent in the response. 
        # The MIME type is part of the HTTP headers and informs the client how to interpret the response body.
        return Response(graphml_data, mimetype='text/plain')

    return k8s_resources_bp