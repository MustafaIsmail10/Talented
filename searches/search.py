import requests
import requests
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Repository Name", "Created Date", "Language", "Stars"]


def search(q):
    url = "https://api.github.com/search/users"
    headers = {"Accept": "application/vnd.github+json"}
    params = {"q": q, "per_page": 50}

    response = requests.get(url=url, headers=headers, params=params)
    data = response.json()
    return data["items"]


def get_skills(repos_url):
    response = requests.get(url=repos_url)
    data = response.json()
    skills = ""
    skill_lst = []
    for repository in data:
        language = repository["language"]
        if language and (language not in skill_lst):
            skills = skills + language + " "
            skill_lst.append(language)
    return skills
