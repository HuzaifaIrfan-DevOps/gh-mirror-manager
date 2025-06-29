import os
import csv
from glob import glob
import pprint

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
    userignore = read_ignore_file('.userignore')
    repoignore = read_ignore_file('.repoignore')
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
