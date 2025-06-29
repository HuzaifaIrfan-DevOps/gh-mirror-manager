import subprocess
import os
from users_repos import users_repos

def main():
    for user, user_repos in users_repos.items():
        user_dir = os.path.join("user", user)
        os.makedirs(user_dir, exist_ok=True)
        for user_repo in user_repos:
            repo_url = f"https://github.com/{user_repo}.git"
            dest_path = os.path.join("user", user_repo)
            if os.path.exists(dest_path):
                print(f"🔄 Updating mirror at {dest_path}")
                subprocess.run(['git', '--git-dir', dest_path, 'remote', 'update', '--prune'], check=True)
            else:
                print(f"Repo {user_repo} not exists in {dest_path}, skipping.")


if __name__ == "__main__":
    main()          

