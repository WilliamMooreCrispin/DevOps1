from github import Github
import yaml
# credentials.yml contains your usr/repo and PAT created in step 11 above
# So we load the data into a YML object
data = yaml.safe_load(open('credentials.yml'))
# Extract the user and token from the data object
# 0. Complete these 2 lines below
# user and token
user = data['creds']['username']
token = data['creds']['token']
# using an access token
g = Github(token)
repo = g.get_repo(user)
## Complete your tasks from here
# 1. Get all branches you have created for your public repo
branches = repo.get_branches()
print("\nBranches:")
for branch in branches:
    print(f"- {branch.name}")
# 2. Get all pull requests you have created
pulls = repo.get_pulls('all')
print("\nPull Requests:")
for pull in pulls:
    print(f"- {pull.title}")
    print(f"-  Number: {pull.number}")
    print(f"-  State: {pull.state}")
    print(f"-  Created By: {pull.user.login}")
# 3. Get a list of commits you have created in your `main` branch.
commits = repo.get_commits()
print("\nCommits in 'main' branch:")
for commit in commits:
    print(commit)