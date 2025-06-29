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

