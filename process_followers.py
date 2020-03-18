from glob import glob
import json


files = glob('followers/*.json')

followers = []
for file in files:
    with open(file, 'r') as f:
        data = json.load(f)
        for user in data['data']['user']['edge_followed_by']['edges']:
            followers.append(
                {
                    'id': user['node']['id'],
                    'username': user['node']['username'],
                    'full_name': user['node']['full_name'],
                    'followed_by_viewer': user['node']['followed_by_viewer']
                }
            )

with open('followers_list.json', 'w') as f:
    json.dump(followers, f, indent=4)
