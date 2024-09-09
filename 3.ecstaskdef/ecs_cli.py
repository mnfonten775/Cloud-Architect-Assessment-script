import subprocess
import sys

def list_ecs_task_definitions(task_definition_family):
    try:
        # Run the AWS CLI command to list task definitions
        result = subprocess.run(
            [
                "aws", "ecs", "list-task-definitions",
                "--family-prefix", task_definition_family,
                "--sort", "DESC",
                "--query", "taskDefinitionArns",
                "--output", "text"
            ],
            capture_output=True, text=True, check=True
        )

        # Print the result
        print("Task Definition Versions for", task_definition_family)
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if the user provided a task definition family name
    if len(sys.argv) != 2:
        print("Usage: python list_ecs_task_definitions.py <task_definition_family>")
        sys.exit(1)

    # Get the task definition family name from the command-line argument
    task_definition_family = sys.argv[1]

    # List the ECS task definitions for the given family
    list_ecs_task_definitions(task_definition_family)

