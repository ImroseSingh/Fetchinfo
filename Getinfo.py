import requests
import json

 class GitHubAPI:

     def __init__(self, id):
         self.id = id      
        

         self.repos = []
         self.commits = {}

     def get_repos(user):
         try:
             r = requests.get(f'https://api.github.com/users/{self.id}/repos')

         except requests.exceptions.HTTPError as error:
             return
         for repo in r.json():
             self.repos.append(repo["name"])
         return self.repos

     def get_commits(user):
         for repo in self.repos:
             try:
                 r = requests.get(f'https://api.github.com/repos/{self.id}/{repo}/commits')
             except requests.exceptions.HTTPError as error:
                 return
             self.commits[repo] = len(r.json())
         return self.commits

    

 if __name__ == "__main__":
     githubapi = GitHubAPI("ImroseSingh")
   
