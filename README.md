# k8s-graphs

1. Visualizer Service: Handles user requests for web pages related to Kubernetes resources.
2. Data-Extraction Service: Fetches specific resource data from the Kubernetes API server.
3. Process Flow
    - User requests a web page from the Visualizer.
    - Visualizer requests specific resource data from Data-Extraction.
    - Data-Extraction queries the Kubernetes API server and returns raw data.
    - Visualizer creates a graph data structure of the requested resource.
    - Visualizer responds to the user with an HTML page displaying the rendered UI graph.


![alt text](images/architecture.svg)
