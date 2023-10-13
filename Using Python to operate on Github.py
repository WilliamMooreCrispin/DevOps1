from github import Github
import yaml
# credentials.yml contains your usr/repo and PAT created in step 11 above
# So we load the data into a YML object
with open('.gitignore', 'r') as file:
    data = yaml.safe_load(file)
# Extract the user and token from the data object
# 0. Complete these 2 lines below
print (data)
token = data['token']
user = data['username']
# using an access token
g = Github(token)
try:
    repo = g.get_repo(user)
    # Rest of your code
except Exception as e:
    print(f"An error occurred: {e}")
## Complete your tasks from here
# 1. Get all branches you have created for your public repo
# 2. Get all pull requests you have created
# 3. Get a list of commits you have created in your `main` branch


