import networkx as nx
import itertools


class GraphCreator:
    def __init__(self):
        self.graph = None
        self.volume_img_url = "https://github.com/kubernetes/community/blob/master/icons/png/resources/labeled/vol-128.png?raw=true"
        self.pod_img_url = "https://github.com/kubernetes/community/blob/master/icons/png/resources/labeled/pod-128.png?raw=true"
        self.green = '#33bbff'
        self.node_size=20

    def add_node(self, node_id, label, image, kind):
        """
        Helper method to add a node to the graph.
        """
        self.graph.add_node(node_id, label=label, shape='image', image=image, kind=kind, size=self.node_size)
    
    def add_edge(self, source, target, color):
        """
        Helper method to add an edge to the graph.
        """
        self.graph.add_edge(source, target, color=color)
    
    def create_pod_graph(self, pod_data) -> nx:
            self.graph = nx.Graph(notebook=True, cdn_resources="in_line", bgcolor="#222222", font_color="white")
            
            for pod in pod_data:
                pod_name = pod['name']
                pod_label = f"{''.join(pod_name.split('-')[:-1])}"
                self.add_node(pod_name, pod_label, self.pod_img_url, "pod")
                
                for volume in pod.get('volume', []):
                    volume_name = f"{volume.get('name')}"
                    volume_label = volume_name
                    
                    if 'projected' in volume.keys():
                        volume_label = f"Projected \n{volume_name}"
                        self.add_node(volume_name, volume_label, self.volume_img_url, "volume")
                        self.add_edge(pod_name, volume_name, self.green)
                        
                        projected_data = volume['projected']['sources']
                        projected_volumes = [ [k for k,v in proj_volume.items() if v is not None] for proj_volume in projected_data]
                        projected_volumes = list(itertools.chain(*projected_volumes))
                        
                        for projected_volume in projected_volumes:
                            projected_node_id = f"{volume_name}-{projected_volume}"
                            self.add_node(projected_node_id, projected_volume, self.volume_img_url, "volume")
                            self.add_edge(volume_name, projected_node_id, self.green)
                    else:
                        self.add_node(volume_name, volume_label, self.volume_img_url, "volume")
                        self.add_edge(pod_name, volume_name, self.green)
            
            return self.graph