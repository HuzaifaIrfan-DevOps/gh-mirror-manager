
from clone_repos import clone_repos
from orgs_repos import orgs_repos

# This script clones repositories for each org listed in orgs_repos.py
def main():
    clone_repos(orgs_repos, path="org")


if __name__ == "__main__":
    main()          

