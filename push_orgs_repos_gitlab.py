
from push_repos_gitlab import push_repos_gitlab
from orgs_repos import orgs_repos


# This script pushes the mirror repositories for each orgs listed in orgs_repos.py to a self-hosted GitLab instance.
def main():
    push_repos_gitlab(orgs_repos, path="org")


if __name__ == "__main__":
    main()