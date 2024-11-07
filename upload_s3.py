import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

def upload_folder_to_s3(folder_path, bucket_name, s3_folder_name=""):
    """
    Upload a folder and its contents to an S3 bucket

    :param folder_path: Path of the folder to upload
    :param bucket_name: Bucket to upload to
    :param s3_folder_name: Folder name in S3 to upload files to (optional)
    :return: True if the folder was uploaded, else False
    """
    # Initialize S3 client with specified credentials
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    
    # Walk through each file in the folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Full path of the file on local
            local_file_path = os.path.join(root, file_name)

            # Define the S3 path (to maintain folder structure)
            relative_path = os.path.relpath(local_file_path, folder_path)
            s3_file_path = os.path.join(s3_folder_name, relative_path).replace("\\", "/")

            try:
                # Upload the file
                s3_client.upload_file(local_file_path, bucket_name, s3_file_path)
                print(f"Uploaded '{local_file_path}' to '{bucket_name}/{s3_file_path}'")
            except FileNotFoundError:
                print(f"The file {local_file_path} was not found.")
                return False
            except NoCredentialsError:
                print("Credentials not available.")
                return False
            except PartialCredentialsError:
                print("Incomplete credentials provided.")
                return False
            except Exception as e:
                print(f"An error occurred while uploading {local_file_path}: {e}")
                return False
    return True

# Usage example:
# Replace 'your_folder_path' with your folder path, and 'makewebev' with your S3 bucket name
# The 's3_folder_name' parameter is optional and will add a prefix folder in S3
# upload_folder_to_s3('your_folder_path', 'makewebev', 'optional-s3-folder')
