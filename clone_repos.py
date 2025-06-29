import subprocess
import os


def clone_repos(keys_repos, path="user"):
    for key, key_repos in keys_repos.items():
        key_dir = os.path.join(path, key)
        os.makedirs(key_dir, exist_ok=True)
        for key_repo in key_repos:
            repo_url = f"https://github.com/{key_repo}.git"
            dest_path = os.path.join(key_dir, key_repo)
            if not os.path.exists(dest_path):
                print(f"Cloning {repo_url} into {dest_path}")
                subprocess.run(["git", "clone", "--mirror", repo_url, dest_path], check=True)
            else:
                print(f"Repo {key_repo} already exists in {dest_path}, skipping.")