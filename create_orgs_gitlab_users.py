
from create_gitlab_users import create_user_if_missing
from orgs_repos import orgs_repos


# This script creates GitLab users based on the organization-repository mapping defined in orgs_repos.py
def main():
    for org in orgs_repos.keys():
        print(f"Processing org: {org}")
        username = org
        email = f"{org}@example.com"
        name = org
        # Example usage
        create_user_if_missing(
            username=username,
            email=email,
            name=name
        )



if __name__ == "__main__":
    main()          





