import requests
import json

 class GitHubAPI:

     def __init__(user, id):
         user.id = id      
        

         user.repos = []
         user.commits = {}

     def get_repos(user):
         try:
             r = requests.get(f'https://api.github.com/users/{self.id}/repos')

         except requests.exceptions.HTTPError as error:
             return
         for repo in r.json():
             user.repos.append(repo["name"])
         return user.repos

     def get_commits(user):
         for repo in user.repos:
             try:
                 r = requests.get(f'https://api.github.com/repos/{self.id}/{repo}/commits')
             except requests.exceptions.HTTPError as error:
                 return
             user.commits[repo] = len(r.json())
         return user.commits

    

 if __name__ == "__main__":
     githubapi = GitHubAPI("ImroseSingh")
   
