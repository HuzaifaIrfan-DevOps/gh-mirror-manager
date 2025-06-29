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
    orgignore = read_ignore_file('org/.orgignore')
    repoignore = read_ignore_file('org/.repoignore')
    return orgignore, repoignore


orgignore, repoignore = get_ignore_lists()
print("Org Ignore List:", orgignore)
print("Repo Ignore List:", repoignore)


def read_orgs_repos_from_csv():
    orgs_repos = {}
    csv_files = glob('org/*.csv')
    for csv_file in csv_files:
        org = os.path.splitext(os.path.basename(csv_file))[0]
        if org in orgignore:
            continue
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            org_repos = []
            for row in reader:
                if not row:
                    continue
                repo = row[0].strip()
                if repo and repo not in repoignore:
                    org_repos.append(repo)
            if org_repos:
                orgs_repos[org] = org_repos
    return orgs_repos

orgs_repos = read_orgs_repos_from_csv()
pprint.pprint(orgs_repos)
