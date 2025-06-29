
from push_repos_gitlab import push_repos_gitlab
from users_repos import users_repos


# This script pushes the mirror repositories for each user listed in users_repos.py to a self-hosted GitLab instance.
def main():
    push_repos_gitlab(users_repos, path="user")


if __name__ == "__main__":
    main()          



