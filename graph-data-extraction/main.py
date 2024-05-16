from kubernetes import client, config
import json
import pprint as pp


def main():
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()

    k8s_client = client.CoreV1Api()
        
    api_resources = k8s_client.get_api_resources()
    # print(type(api_resources))
    # print(dir(api_resources))

    # print(type(api_resources.resources))
   
    resources_list = [(resource.kind,resource.name) for resource in   api_resources.resources]
    
    
    pp.pprint(resources_list)
    print(f"{ len(resources_list) = }")
        
    for item in api_resources.resources:
        if item.kind == "Namespace":
            print(item)
    
    

if __name__ == '__main__':
    main()