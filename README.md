<div align="center">
  <h1>gh-mirror-manager</h1>
  <p><h3 align="center">Mirror All Github User and User Orgs's Repos to Gitlab 🚀</h3></p>
</div>


•
<hr>

## Demo Video

[![Demo Video](https://img.youtube.com/vi/EJNBFAzJQYY/0.jpg)](https://www.youtube.com/watch?v=EJNBFAzJQYY)


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




## 🤝🏻 &nbsp;Connect with Me

<p align="center">
<a href="https://www.huzaifairfan.com"><img src="https://img.shields.io/badge/-huzaifairfan.com-1aa260?style=flat&logo=Google-Chrome&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/huzaifairfan/"><img src="https://img.shields.io/badge/-Huzaifa%20Irfan-0072b1?style=flat&logo=Linkedin&logoColor=white"/></a>
<a href="https://github.com/HuzaifaIrfan/"><img src="https://img.shields.io/badge/-Huzaifa%20Irfan-4078c0?style=flat&logo=Github&logoColor=white"/></a>
<a href="mailto:contact@huzaifairfan.com"><img src="https://img.shields.io/badge/-contact@huzaifairfan.com-c71610?style=flat&logo=Gmail&logoColor=white"/></a>
</p>

## License

Licensed under the MIT License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)