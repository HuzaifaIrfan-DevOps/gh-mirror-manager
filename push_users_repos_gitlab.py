import subprocess
import os
from users_repos import users_repos

from dotenv import load_dotenv
import os 
# Load environment variables from .env file
load_dotenv(override=True)

GITLAB_URL = os.getenv("GITLAB_URL", "http://localhost/")

# This script pushes the mirror repositories for each user listed in users_repos.py to a self-hosted GitLab instance.
def main():
    for user, user_repos in users_repos.items():
        user_dir = os.path.join("user", user)
        os.makedirs(user_dir, exist_ok=True)
        for user_repo in user_repos:
            # repo_url = f"https://github.com/{user_repo}.git"
            
            # Only insert "dot" after "/" if there is a "." immediately after the "/"
            user_part, repo_part = user_repo.split('/', 1)
            if repo_part[0] == ".":
                user_repo_gitlab = f"{user_part}/dot{repo_part}"
            else:
                user_repo_gitlab = user_repo

            dest_path = os.path.join("user", user_repo)
            if os.path.exists(dest_path):
                # Push to GitLab self-hosted
                target_url = f"{GITLAB_URL}/{user_repo_gitlab}.git"
                print(f"🚀 Pushing to: {target_url}")
                # subprocess.run(['git', '--git-dir', dest_path, 'push', '--mirror', target_url], check=True)
                subprocess.run(['git', '--git-dir', dest_path, 'push', '--all', target_url], check=True)
                # subprocess.run(['git', '--git-dir', dest_path, 'push', '--tags', target_url], check=True)
            else:
                print(f"Repo {user_repo} not exists in {dest_path}, skipping.")


if __name__ == "__main__":
    main()          



