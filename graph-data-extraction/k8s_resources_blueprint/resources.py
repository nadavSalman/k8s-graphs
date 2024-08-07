from flask import Blueprint, render_template, jsonify, request
from flask import current_app
from graph_data_extraction.data_extraction import K8sResourcesDataExtraction
from kubernetes import client, config


def create_resources_bp(resource_type: str,k8s_client: client.CoreV1Api) -> Blueprint:
    k8s_resources_bp = Blueprint(resource_type,__name__)
    k8s_exctractor = K8sResourcesDataExtraction()
     
    @k8s_resources_bp.route(f'/{resource_type.lower()}', methods=["GET"])
    def get_resource():
        current_app.logger.info(f"GET request received for {resource_type} resource")
        extracted_data = k8s_exctractor.solve_for(
            name = 'extracted_pods_data',
            k8s_client=k8s_client)
        current_app.logger.info(f"extracted_data - {extracted_data}")

        if extracted_data != {}:
            return jsonify(extracted_data), 200
        else:
            return jsonify({
                "Error : Resource data not found."
            }), 404

    return k8s_resources_bp