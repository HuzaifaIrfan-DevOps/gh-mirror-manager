import requests

from dotenv import load_dotenv
import os 
# Load environment variables from .env file
load_dotenv(override=True)

USERNAME="root"
GITLAB_URL = "http://192.168.18.215"
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")

HEADERS = {"PRIVATE-TOKEN": GITLAB_TOKEN}


def user_exists(username):
    r = requests.get(f"{GITLAB_URL}/api/v4/users?username={username}", headers=HEADERS)
    return r.json()[0] if r.status_code == 200 and r.json() else None


def create_user_if_missing(username, email, name, password="changeme123", skip_confirmation=True):
    if user_exists(username):
        print(f"✅ User '{username}' already exists.")
        return

    data = {
        "email": email,
        "username": username,
        "name": name,
        "password": password,
        "skip_confirmation": skip_confirmation,
    }

    r = requests.post(f"{GITLAB_URL}/api/v4/users", headers=HEADERS, json=data)
    if r.status_code == 201:
        print(f"👤 Created user: {username}")
    else:
        print(f"❌ Failed to create user: {r.status_code} - {r.text}")




import os
import csv
from glob import glob
import pprint
import subprocess

def read_ignore_file(filename):
    ignore_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_list.append(line)
    return ignore_list

def get_ignore_lists():
    userignore = read_ignore_file('user/.userignore')
    repoignore = read_ignore_file('user/.repoignore')
    return userignore, repoignore


userignore, repoignore = get_ignore_lists()
print("User Ignore List:", userignore)
print("Repo Ignore List:", repoignore)


def read_users_repos_from_csv():
    users_repos = {}
    csv_files = glob('user/*.csv')
    for csv_file in csv_files:
        user = os.path.splitext(os.path.basename(csv_file))[0]
        if user in userignore:
            continue
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            user_repos = []
            for row in reader:
                if not row:
                    continue
                repo = row[0].strip()
                if repo and repo not in repoignore:
                    user_repos.append(repo)
            if user_repos:
                users_repos[user] = user_repos
    return users_repos

users_repos = read_users_repos_from_csv()
pprint.pprint(users_repos)

def main():
    for user in users_repos.keys():
        print(f"Processing user: {user}")
        username = user
        email = f"{user}@example.com"
        name = user
        # Example usage
        create_user_if_missing(
            username=username,
            email=email,
            name=name
        )


if __name__ == "__main__":
    main()          





