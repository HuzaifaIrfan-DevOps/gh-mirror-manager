import requests

from dotenv import load_dotenv
import os 
# Load environment variables from .env file
load_dotenv(override=True)

USERNAME="root"

GITLAB_URL = os.getenv("GITLAB_URL", "http://localhost")
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN", "glpat-")

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






