k8s_supported_resources  = {
    "Pod": {
        "api_version": "v1"
    },
    "ReplicaSet": {
        "api_version": "apps/v1"
    },
    "Deployment": {
        "api_version": "apps/v1"
    },
    "StatefulSet": {
        "api_version": "apps/v1"
    },
    "Service": {
        "api_version": "v1"
    },
    "Ingress": {
        "api_version": "networking.k8s.io/v1"
    },
    "Node": {
        "api_version": "v1"
    },
    "pv": {
        "api_version": "v1"
    },
    "pvc": {
        "api_version": "v1"
    }
}