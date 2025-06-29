
from update_repos import update_repos
from orgs_repos import orgs_repos

# This script updates the mirror repositories for each organization listed in orgs_repos.py
def main():
    update_repos(orgs_repos, path="org",)


if __name__ == "__main__":
    main()
