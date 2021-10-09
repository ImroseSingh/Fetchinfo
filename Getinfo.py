import requests
import json
from unittest import mock

class GitHubAPI:
    
    def __init__(user, id):
        user.id = id      
        

        user.repos = []
        user.commits = {}

    def get_repos(user):
        try:
            r = requests.get(f'https://api.github.com/users/{user.id}/repos')
            
        except requests.exceptions as error:
            return
        for repo in r.json():
            user.repos.append(repo["name"])
        return user.repos

    def get_commits(user):
        for repo in user.repos:
            try:
                r = requests.get(f'https://api.github.com/repos/{user.id}/{repo}/commits')
            except requests.exceptions as error:
                return
            user.commits[repo] = len(r.json())
        return user.commits

    def print_data(user):
        for repo in user.repos:
            print(f'Repo: {repo} Number of commits: {user.commits[repo]}')

   

if __name__ == "__main__":
    githubapi = GitHubAPI("ImroseSingh")
   
