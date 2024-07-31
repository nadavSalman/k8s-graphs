from graph_data_extraction.pod_scrape import *

# from kubernetes import client, config
import json
import pprint as pp




# def extracted_pods_data(k8s_client: client.CoreV1Api):
#     all_namespases_pods: list = k8s_client.list_pod_for_all_namespaces().to_dict().get('items')
#     all_pods_extract_data = []
#     for pod in all_namespases_pods:
#         pod_volumes = []
        
#         # crean not extis volumes
#         for volume in pod['spec']['volumes']:
#             instance_volume = {
#                 'name': volume['name']
#             }
#             for key, value in volume.items():
#                 if value is not None:
#                     instance_volume[key] = value
#             pod_volumes.append(instance_volume)
            
#         all_pods_extract_data.append( {
#             'name': pod['metadata']['name'],
#             'namespace': pod['metadata']['namespace'],
#             'labels': pod['metadata']['labels'],
#             'volume': pod_volumes,
#         })
#     return all_pods_extract_data
    

def main():
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()
    k8s_client = client.CoreV1Api()
        
    all_pods_extract_data = extracted_pods_data(k8s_client)
    pp.pprint(all_pods_extract_data[-1])
    
    
if __name__ == '__main__':
    main()