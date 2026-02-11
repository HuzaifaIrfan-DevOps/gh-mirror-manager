
rm -rf user/*.csv
rm -rf org/*.csv

uv run get_users_and_user_orgs_repos.py

uv run clone_users_repos.py
# uv run clone_orgs_repos.py

uv run update_users_repos.py
# uv run update_orgs_repos.py

uv run create_users_gitlab_users.py
# uv run create_orgs_gitlab_users.py

uv run push_users_repos_gitlab.py
# uv run push_orgs_repos_gitlab.py