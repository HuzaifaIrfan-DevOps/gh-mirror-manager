from github import Github

# Authentication is defined via github.Auth
from github import Auth

import csv

from pathlib import Path

# Create a new folder if it doesn't exist
def create_folder(folder_name):
    # Define the folder path
    folder_path = Path(folder_name)

    # Create the folder
    folder_path.mkdir(parents=True, exist_ok=True)

    print(f"Folder created at: {folder_path}")
    
    return folder_path

from dotenv import load_dotenv
import os 
# Load environment variables from .env file
load_dotenv(override=True)

USERNAME=os.getenv("USERNAME")
PERSONAL_ACCESS_TOKEN=os.getenv("PERSONAL_ACCESS_TOKEN")
# print(USERNAME)
# print(PERSONAL_ACCESS_TOKEN)
# using an access token
auth = Auth.Token(PERSONAL_ACCESS_TOKEN)


# First create a Github instance:

# Public Web Github
gh = Github(auth=auth)

# Github Enterprise with custom hostname
# gh = Github(base_url="https://{hostname}/api/v3", auth=auth)

# Then play with your Github objects:
print("Logined User:", gh.get_user().login)
# Print user's repositories
print("User's Repositories:")
for repo in gh.get_user().get_repos():
    user=repo.owner.login
    full_name=repo.full_name
    print("User:", user)
    print("Repo Full Name:", full_name)

    # Ensure the directory exists
    os.makedirs(f"user", exist_ok=True)

    # File path
    file_path = f"user/{user}.csv"

    # Check if full_name already exists in the file
    exists = False
    if os.path.exists(file_path):
        with open(file_path, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            exists = any(full_name in row for row in reader)

    # Append if it doesn't already exist
    if not exists:
        with open(file_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([full_name])

print("User's Organizations:")
for org in gh.get_user().get_orgs():
    org_name = org.login
    print("---- Organization Name:", org_name)
    print("---- Organization's Repositories:")
    for repo in org.get_repos():
        full_name=repo.full_name
        print("Repo Full Name:", full_name)

        # Ensure the directory exists
        os.makedirs(f"org", exist_ok=True)

        # File path
        file_path = f"org/{org_name}.csv"

        # Check if full_name already exists in the file
        exists = False
        if os.path.exists(file_path):
            with open(file_path, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                exists = any(full_name in row for row in reader)

        # Append if it doesn't already exist
        if not exists:
            with open(file_path, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([full_name])

# To close connections after use
gh.close()