
from update_repos import update_repos
from users_repos import users_repos

# This script updates the mirror repositories for each user listed in users_repos.py
def main():
    update_repos(users_repos, path="user",)


if __name__ == "__main__":
    main()          

