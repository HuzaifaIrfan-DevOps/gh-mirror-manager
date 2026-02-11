
rm -rf user/*.csv
rm -rf org/*.csv

uv run get_users_and_user_orgs_repos.py

uv run clone_users_repos.py
# uv run clone_orgs_repos.py

uv run update_users_repos.py
# uv run update_orgs_repos.py