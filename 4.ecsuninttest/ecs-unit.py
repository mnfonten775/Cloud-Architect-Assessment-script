import unittest
from unittest.mock import patch, MagicMock
from ecs import create_ecs_cluster, register_task_definition, list_ecs_clusters

class TestECSFunctions(unittest.TestCase):

    @patch('ecs.boto3.client')  # Mocking the boto3 ECS client
    def test_create_ecs_cluster(self, mock_boto_client):
        # Set up the mock client and response
        mock_ecs_client = MagicMock()
        mock_boto_client.return_value = mock_ecs_client
        mock_ecs_client.create_cluster.return_value = {'cluster': {'clusterName': 'my-cluster'}}

        # Call the function
        response = create_ecs_cluster('my-cluster')

        # Assertions
        mock_ecs_client.create_cluster.assert_called_once_with(clusterName='my-cluster')
        self.assertEqual(response['cluster']['clusterName'], 'my-cluster')

    @patch('ecs.boto3.client')  # Mocking the boto3 ECS client
    def test_register_task_definition(self, mock_boto_client):
        # Set up the mock client and response
        mock_ecs_client = MagicMock()
        mock_boto_client.return_value = mock_ecs_client
        mock_ecs_client.register_task_definition.return_value = {'taskDefinition': {'family': 'my-family'}}

        # Call the function
        container_definitions = [{"name": "my-container", "image": "nginx"}]
        response = register_task_definition('my-family', container_definitions)

        # Assertions
        mock_ecs_client.register_task_definition.assert_called_once_with(
            family='my-family',
            containerDefinitions=container_definitions
        )
        self.assertEqual(response['taskDefinition']['family'], 'my-family')

    @patch('ecs.boto3.client')  # Mocking the boto3 ECS client
    def test_list_ecs_clusters(self, mock_boto_client):
        # Set up the mock client and response
        mock_ecs_client = MagicMock()
        mock_boto_client.return_value = mock_ecs_client
        mock_ecs_client.list_clusters.return_value = {'clusterArns': ['arn:aws:ecs:us-west-2:123456789012:cluster/my-cluster']}

        # Call the function
        clusters = list_ecs_clusters()

        # Assertions
        mock_ecs_client.list_clusters.assert_called_once()
        self.assertEqual(clusters, ['arn:aws:ecs:us-west-2:123456789012:cluster/my-cluster'])

if __name__ == '__main__':
    unittest.main()

