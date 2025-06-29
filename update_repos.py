import subprocess
import os

def update_repos(keys_repos, path="user"):
    for key, key_repos in keys_repos.items():
        path_key_dir = os.path.join(path, key)
        os.makedirs(path_key_dir, exist_ok=True)
        for key_repo in key_repos:
            repo_url = f"https://github.com/{key_repo}.git"
            dest_path = os.path.join(path, key_repo)
            if os.path.exists(dest_path):
                print(f"🔄 Updating mirror at {dest_path}")
                subprocess.run(['git', '--git-dir', dest_path, 'remote', 'update', '--prune'], check=True)
            else:
                print(f"Repo {key_repo} not exists in {dest_path}, skipping.")

