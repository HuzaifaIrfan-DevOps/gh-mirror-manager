
from clone_repos import clone_repos
from users_repos import users_repos

# This script clones repositories for each user listed in users_repos.py
def main():
    clone_repos(users_repos, path="user")


if __name__ == "__main__":
    main()          

