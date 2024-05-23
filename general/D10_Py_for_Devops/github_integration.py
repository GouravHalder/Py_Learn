""" Pull req testing"""
"""Had to do pip install requests"""
import requests
import pprint
"""/repos/{owner}/{repo}/pulls is the template 
from https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28"""
response=requests.get("https://api.github.com/repos/GouravHalder/Py_Learn/pulls")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    pull_requests = response.json()
    
    # Pretty-print the JSON response
    pprint.pprint(pull_requests)
    
    # Accessing and printing the 'id' of the first pull request
    if pull_requests:
        print(f"Title of the first Release version 1.0.0 pull request: {pull_requests[0]['title']}")
    else:
        print("No pull requests found.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")