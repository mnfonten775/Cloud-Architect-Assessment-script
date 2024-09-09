import argparse
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Function to list files in an S3 bucket
def list_files(args):
    s3 = boto3.client('s3')

    try:
        response = s3.list_objects_v2(Bucket=args.bucket)

        if 'Contents' in response:
            print(f"Files in bucket {args.bucket}:")
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f"No files found in bucket {args.bucket}.")
    except NoCredentialsError:
        print("Error: No AWS credentials found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials found.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Main function to set up the argument parser
def main():
    parser = argparse.ArgumentParser(description='Simple CLI to interact with AWS S3')

    # Add a command to list files in an S3 bucket
    subparsers = parser.add_subparsers()

    parser_list = subparsers.add_parser('list-files', help='List files in an S3 bucket')
    parser_list.add_argument('--bucket', required=True, help='The name of the S3 bucket')
    parser_list.set_defaults(func=list_files)

    # Parse the arguments and call the appropriate function
    args = parser.parse_args()

    # Call the function associated with the command
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

