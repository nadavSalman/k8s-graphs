from kubernetes import client, config
import json
import pprint as pp
from flask import current_app
from pyvis import network as net
from  graph_data_extraction.graph_creator import GraphCreator


class K8sResourcesDataExtraction:

    def __init__(self):
        self.doc_str = ""  

    def extracted_pods_data(self, k8s_client: client.CoreV1Api):
        all_namespases_pods: list = k8s_client.list_pod_for_all_namespaces().to_dict().get('items')
        all_pods_extract_data = []
        for pod in all_namespases_pods:
            pod_volumes = []
            
            # crean not extis volumes
            for volume in pod['spec']['volumes']:
                instance_volume = {
                    'name': volume['name']
                }
                for key, value in volume.items():
                    if value is not None:
                        instance_volume[key] = value
                pod_volumes.append(instance_volume)
                
            all_pods_extract_data.append( {
                'name': pod['metadata']['name'],
                'namespace': pod['metadata']['namespace'],
                'labels': pod['metadata']['labels'],
                'volume': pod_volumes,
            })

        # return pyvis graph object
        graph_creator = GraphCreator()        
        graph:net = graph_creator.create_pod_graph(pod_data=all_pods_extract_data)

        
        # return all_pods_extract_data
        return graph
    
    # Dynamic function call resolver   
    def solve_for(self, name: str, *args, **kwargs):
        if hasattr(self, name) and callable(func := getattr(self, name)):
            current_app.logger.info(f"Resolve function for resource : {name}")
            return func(*args, **kwargs)
        else:
            current_app.logger.error(f"Faile to resolve function for resource : {name}")