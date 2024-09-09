import boto3

def create_ecs_cluster(cluster_name):
    client = boto3.client('ecs')
    response = client.create_cluster(clusterName=cluster_name)
    return response

def register_task_definition(family, container_definitions):
    client = boto3.client('ecs')
    response = client.register_task_definition(
        family=family,
        containerDefinitions=container_definitions
    )
    return response

def list_ecs_clusters():
    client = boto3.client('ecs')
    response = client.list_clusters()
    return response.get('clusterArns', [])

