
from create_gitlab_users import create_user_if_missing
from users_repos import users_repos


# This script creates GitLab users based on the user-repository mapping defined in users_repos.py
def main():
    for user in users_repos.keys():
        print(f"Processing user: {user}")
        username = user
        email = f"{user}@example.com"
        name = user
        # Example usage
        create_user_if_missing(
            username=username,
            email=email,
            name=name
        )        


if __name__ == "__main__":
    main()          





