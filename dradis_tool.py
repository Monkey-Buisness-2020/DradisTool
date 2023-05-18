# This is a tool to work with the Dradis API.
import requests
import json
from termcolor import colored
from config import api_key, server_addr

'''
To-Do List:
- List Projects and their ID's
- Add issues to a project from the library
'''

dradis_api = f"{api_key}"
header = {'Accept': 'application/vnd.dradisapi; v=2', 'Authorization': f'Token token={dradis_api}'}
project_url = f"https://{server_addr}/pro/api/projects"
issues_url = f"https://{server_addr}/pro/api/issues"

response = requests.get(project_url, headers=header, verify=False)
data = json.loads(response.text)

print("\nProjects\n")

for details in data:
    print(f"ID: {details['id']} - {details['name']}")
else:
    print("No Projects found or some kind of issue was found")

id_number = input("\nPlease enter an ID then press ENTER: ")

issues_response = requests.get(issues_url, headers={'Accept': 'application/vnd.dradisapi; v=2', 'Authorization': f'Token token={dradis_api}', 'Dradis-Project-Id': f'{id_number}'}, verify=False)
issues_data = json.loads(issues_response.text)

for issues in issues_data:
    for tag_colour in issues['tags']:
        if tag_colour['display_name'] == 'Critical':
            print('CRITICIAL: ' + colored(issues['title'], 'magenta')) # Print this title in corresponding colour
        elif tag_colour['display_name'] == 'High':
            print('HIGH: ' + colored(issues['title'], 'red')) 
        elif tag_colour['display_name'] == 'Medium':
            print('MEDIUM: ' + colored(issues['title'], 'yellow'))
        elif tag_colour['display_name'] == 'Low':
            print('LOW: ' + colored(issues['title'], 'blue'))
        elif tag_colour['display_name'] == 'Info':
            print('INFO: ' + colored(issues['title'], 'green'))
        else:
            print("\nNo Tags were found\n")
