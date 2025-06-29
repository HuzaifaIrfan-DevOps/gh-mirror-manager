import subprocess
import os
from users_repos import users_repos

# This script clones repositories for each user listed in users_repos.py
def main():
    for user, user_repos in users_repos.items():
        user_dir = os.path.join("user", user)
        os.makedirs(user_dir, exist_ok=True)
        for user_repo in user_repos:
            repo_url = f"https://github.com/{user_repo}.git"
            dest_path = os.path.join("user", user_repo)
            if not os.path.exists(dest_path):
                print(f"Cloning {repo_url} into {dest_path}")
                subprocess.run(["git", "clone", "--mirror", repo_url, dest_path], check=True)
            else:
                print(f"Repo {user_repo} already exists in {dest_path}, skipping.")


if __name__ == "__main__":
    main()          

