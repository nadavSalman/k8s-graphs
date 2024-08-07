from kubernetes import client, config
from flask import Flask, render_template, request
from k8s_resources_blueprint.resources import create_resources_bp

app = Flask(__name__)
config.load_kube_config()
k8s_client = client.CoreV1Api()

app.register_blueprint(
    create_resources_bp(
        resource_type='pod',
        k8s_client=k8s_client,
    )
)