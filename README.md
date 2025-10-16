<div align="center">
  <h1>gh-mirror-manager</h1>
  <p><h3 align="center">Mirror All Github User and User Orgs's Repos to Gitlab 🚀</h3></p>
</div>


•
<hr>

## 🎬 Demo

[▶️![Demo](https://img.youtube.com/vi/EJNBFAzJQYY/maxresdefault.jpg)](https://www.youtube.com/watch?v=EJNBFAzJQYY)


# 🚀 Usage

## Copy .env and .ignores

```sh
cp .env.example .env
cp .userignore.example .userignore
cp .orgignore.example .orgignore
cp .repoignore.example .repoignore
```

## Get User and Org Repos Listing

```sh
uv run get_users_and_user_orgs_repos.py
```

- Edit .repoignore to ignore repo
- Edit .userignore to ignore user
- Edit .orgignore to ignore org


## First Time Clone User Repos

```sh
uv run clone_users_repos.py
uv run clone_orgs_repos.py
```

## Update User Repos

```sh
uv run update_users_repos.py
uv run update_orgs_repos.py
```

## Create User Gitlab
- Set Default Repo Branch Protection to Instance Admin

```sh
uv run create_users_gitlab_users.py
uv run create_orgs_gitlab_users.py
```
## Push User Repos Gitlab

```sh
uv run push_users_repos_gitlab.py
uv run push_orgs_repos_gitlab.py
```

## Run

```sh
sh get_clone_update_push.sh
```





# 📝 Documentation

# 📚 References


# 🤝🏻 Connect with Me

[![GitHub](https://img.shields.io/badge/Github-%23222.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HuzaifaIrfan/)
[![Website](https://img.shields.io/badge/Website-%23222.svg?style=for-the-badge&logo=google-chrome&logoColor==%234285F4)](https://www.huzaifairfan.com)

# 📜 License

Licensed under the GPL3 License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)

Last Updated on 2025-07-29
