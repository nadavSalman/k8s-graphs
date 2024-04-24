from flask import Flask, render_template, request
from pyvis.network import Network
import networkx as nx
import os
from k8s_resources.resources import create_resources_bp
from resources_inventory.incentory import k8s_supported_resources
from graph_generator.generator import GraphGenerator, create_network_graph
# import pandas as pd



app = Flask(__name__)




def delete_files_in_templates_directory():
    # Delete all files inside the templates directory to force reerendering of the graph fro new requests.
    template_dir = os.path.join(os.getcwd(), 'templates')
    for file_name in os.listdir(template_dir):
        file_path = os.path.join(template_dir, file_name)
        os.remove(file_path)

@app.after_request
def call_delete_files_in_templates_directory(response):
    delete_files_in_templates_directory()
    app.logger.info("Deleted all files in the templates directory.")
    return response


# def create_network_graph(number_of_nodes,current_route):
#     statis_file_name = "network-graph.html"
#     g = Network(notebook=True,
#             cdn_resources="remote",
#             height="1000px",
#             width="100%",
#             bgcolor="#222222", 
#             font_color="white")
#     # g = Network(notebook=True,
#     #             cdn_resources="remote",
#     #             height="750px",
#     #             width="100%",
#     #             select_menu=True,
#     #             filter_menu=True,
#     #             bgcolor="#222222", 
#     #             font_color="white")
#     nxg = nx.complete_graph(number_of_nodes)
#     g.from_nx(nxg)
#     g.show_buttons(filter_=['physics'])
#     statis_file_name = statis_file_name.split(".")[0] + f"-{current_route}.html"
#     full_path = f"{os.getcwd()}/templates/{statis_file_name}"
#     print(f"{full_path =}")
#     g.show(full_path)
#     app.logger.info(f"Created network graph at templates/{statis_file_name}, with {number_of_nodes} nodes.")
#     return statis_file_name

# @app.route("/test-a")
# def test_a():
#     # number_of_nodes = 10
#     # g = Network(notebook=True,
#     #         cdn_resources="remote",
#     #         height="1000px",
#     #         width="100%",
#     #         bgcolor="#222222", 
#     #         font_color="white")
#     # nxg = nx.complete_graph(number_of_nodes)
#     # g.from_nx(nxg)
#     # g.show_buttons(filter_=['physics'])
    
#     # generator = GraphGenerator(g)
#     # template_full_path = generator.generate("test-a")
#     # app.logger.info("Rendering template: " + template_full_path)
#     # return render_template("/home/nadav/dev-me/pyvis-jupyter-notebook/graph-visualizer/templates/test-a.html")
    

    
#     current_route = request.path.split("/")[-1]
#     return render_template(create_network_graph(10,current_route))


# @app.route("/test-b")
# def test_b():
#     current_route = request.path.split("/")[-1]
#     return render_template(create_network_graph(5,current_route))



# @app.route("/test-c")
# def test_c():
#     net = Network(notebook=True,
#             cdn_resources="remote",
#             height="1000px",
#             width="100%",
#             bgcolor="#222222", 
#             font_color="white")
#     number_of_low_lwvwl_nodes = 101
#     net.add_nodes(
#         [id for id in range(1,number_of_low_lwvwl_nodes)],
#         label= [ f"Pod_{id}" for id in (range(1,number_of_low_lwvwl_nodes))],
#         color=["#00E5FF" for id in range(1,number_of_low_lwvwl_nodes)]
#     )
#     net.add_node(12,label="root",color="green",value=50)
#     net.add_node(number_of_low_lwvwl_nodes,label="base",color="#FF0000",value=50)
#     net.add_edge(12,number_of_low_lwvwl_nodes)
    
    
#     for i in range(1,number_of_low_lwvwl_nodes):
#         net.add_edge(number_of_low_lwvwl_nodes,i)
#         for j in range(1,number_of_low_lwvwl_nodes):
#             if i % 2 == 0 and j % 2 == 0 and i != j:
#                 net.add_edge(i,j)
#             elif i % 2 != 0 and j % 2 != 0 and i != j:
#                 net.add_edge(i,j)
#     net.add_node(12,label="root-A",color="green",value=50)
#     net.add_edge(12,number_of_low_lwvwl_nodes)
    
#     full_path = f"{os.getcwd()}/templates/test-c.html"
#     app.logger.info(f"file full path {full_path =}")
#     net.show_buttons(filter_=['physics'])
#     net.show(full_path)
#     app.logger.info(f"Created network graph at templates/test-c.html") 
    

#     return render_template("test-c.html")


# @app.route("/test-d")
# def test_d():
    
    
#     from pyvis.network import Network

#     # create pyvis Network object
#     net = Network(height = "500px", width = "600px", notebook = True)

#     # import karate graph
#     net.from_nx(karate)
#     net.show('out1.html')
    
    
#     net = Network(notebook=True,
#             cdn_resources="remote",
#             height="1000px",
#             width="100%",
#             bgcolor="#222222", 
#             font_color="white")
#     net.show_buttons(filter_=['physics'])
#     net.toggle_drag_nodes(True)
#     net.barnes_hut()
#     net.from_nx(nx.davis_southern_women_graph())
#     file_name = "test-d.html"
#     full_path = f"{os.getcwd()}/templates/{file_name}"
#     net.show(full_path)
#     return render_template(file_name)





# pod_resource_name = "Pod"
# app.register_blueprint(
#     create_resources_bp(
#         resource_type=pod_resource_name,
#         bp_name=pod_resource_name
#     ),
#     url_prefix="/resources"
# )

# deployment_resource_name = "Deployment"
# app.register_blueprint(
#     create_resources_bp(
#         resource_type=deployment_resource_name,
#         bp_name=deployment_resource_name
#     ),
#     url_prefix="/resources"
# )



for resource in k8s_supported_resources.keys():
    app.register_blueprint(
        create_resources_bp(
            resource_type=resource,
            bp_name=resource
        ),
        url_prefix="/resources"
    )
    
    
@app.route("/endpoints")
def endpoints():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append(str(rule))
    return {"endpoints": routes}