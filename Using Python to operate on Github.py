from github import Github
import yaml
from github import Auth

# credentials.yml contains  your  usr/repo  and  PAT  created  in  step  11  above
# So we load the data into a YML object
with open("credentials.yml", 'r') as stream:
    data = yaml.safe_load(stream)

auth = Auth.Token(data['creds']['token'])

# Public Web Github
g = Github(auth=auth)

# Get the authenticated user (you)
user = g.get_user()

# 1. Get all branches you have created for your public repo
repos = user.get_repos(affiliation='owner')
branches = []
for repo in repos:  # Loop through each insolent in the repo
    repo_name = repo.name
    repo_owner = repo.owner.login
    for branch in repo.get_branches():
        branches.append(f"{repo_owner}/{repo_name}/{branch.name}")
print("Branches you have created:")
for branch in branches:
    print(branch)

# 2. Get all pull requests you have created
created_pulls = []

for branch in branches:
    repo_owner, repo_name, branch_name = branch.split('/')
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    pulls = repo.get_pulls(state='all', head=f"{repo_owner}:{branch_name}")
    created_pulls.extend(pulls)
print("\nPull requests you have created:")
for pull in created_pulls:
    print(f"{pull.base.repo.owner.login}/{pull.base.repo.name} - #{pull.number}: {pull.title}")

# 3. Get a list of commits you have created in your `main` branch
main_commits = []

for branch in branches:
    repo_owner, repo_name, branch_name = branch.split('/')
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    try:
        commits = repo.get_commits(sha=f"heads/{branch_name}")
        for commit in commits:
            if commit.author.login == user.login:
                main_commits.append(commit.sha)
    except:
        pass

print("\nCommits you have created in `main` branch:")
for commit_sha in main_commits:
    print(commit_sha)
g.close()
