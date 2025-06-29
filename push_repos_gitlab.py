import subprocess
import os

from dotenv import load_dotenv
import os 
# Load environment variables from .env file
load_dotenv(override=True)

GITLAB_URL = os.getenv("GITLAB_URL", "http://localhost/")

# This script pushes the mirror repositories for each user listed in users_repos.py to a self-hosted GitLab instance.
def push_repos_gitlab(keys_repos, path="user"):
    for key, key_repos in keys_repos.items():
        path_key_dir = os.path.join(path, key)
        os.makedirs(path_key_dir, exist_ok=True)
        for key_repo in key_repos:
            # repo_url = f"https://github.com/{user_repo}.git"
            
            # Only insert "dot" after "/" if there is a "." immediately after the "/"
            user_part, repo_part = key_repo.split('/', 1)
            if repo_part[0] == ".":
                user_repo_gitlab = f"{user_part}/dot{repo_part}"
            else:
                user_repo_gitlab = key_repo

            path_key_repo_destination = os.path.join(path, key_repo)
            if os.path.exists(path_key_repo_destination):
                # Push to GitLab self-hosted
                target_url = f"{GITLAB_URL}/{user_repo_gitlab}.git"
                print(f"🚀 Pushing to: {target_url}")
                # subprocess.run(['git', '--git-dir', dest_path, 'push', '--mirror', target_url], check=True)
                subprocess.run(['git', '--git-dir', path_key_repo_destination, 'push', '--all', target_url], check=True)
                # subprocess.run(['git', '--git-dir', dest_path, 'push', '--tags', target_url], check=True)
            else:
                print(f"Repo {key_repo} not exists in {path_key_repo_destination}, skipping.")


if __name__ == "__main__":
    main()          



