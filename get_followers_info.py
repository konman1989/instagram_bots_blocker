import csv
import json
import time
import requests

headers = {
    'authority': 'www.instagram.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
    'cookie': 'mid=W0S8nQAEAAGgkxjmeT_Ay7SjESHR; mcd=3; fbm_124024574287414=base_domain=.instagram.com; ig_did=D4B7081B-405D-4CAC-8E16-3C007DF1F2EC; fbsr_124024574287414=0hG9pveZtZ-5xJ83EE3WFcabRBSAc30_A6qrBEs6eBs.eyJ1c2VyX2lkIjoiMTAwMDAxMjg0NDM0MDcxIiwiY29kZSI6IkFRQVdQcEdjWm5pc0M3SUR4Ym9yWW5BRzFwa2plRFpFU1BGYlItMzB4SWNGQ2xDa3QxV1NvV0VQbjc0aEMzdF90Mkx2eDVNeV9Od3p4dk11NGtJOTBPeEtaNk1uMUt3SDN6Z200MWdxNkt4eDVCWWxZZ1FBekRIU1VZTGpYOURnWWR4MkNHT20yYVcxRVdqNUFyUnE1SGo0UnMwMXVPM2p2T1Zta0pTVHBLWjl6N0VJWTRlRWt0UVdGWGNsLTg3RVhZUE1ZODBZZXhnLWl3T2hHVGxUWDVzSzF1MDJuQWZleklTNy1BbGhGVTdxbXl4T0ppcWFVczMxbHV4V3JONXppZ1cxYmhnY0NFSDA5aWxmRl9FblNSZXhxRWFRYVhOcVROUmxNWF96RUV5cXZrV0hLd1hJYnZ1dGlWcWVSaUVVdDZaN003Ml9yaTlGQWt6bGhuaFRqUzVYIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUV0djdKeW5aQUpQWkJLY1V3d2xReTFDVVpCb2dHM0daQXVyMzdSZTBvNlBBN2F0VFpDWHBSQjBKRDFCRXZJNTVUWHdta3I2cUxPR3RmUkJ5SVRsWkM2RXp2NHZGZTY2R29mY0lMeUJIbGI1T2Q5SkxhdzZFYVNIVVpDV2xZWkNiQ1pBSG1GR1VveGJqOXVsQjl4eGNub2pqczgxcFIxZWptakRiY012N1BGelQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTU4NDI3MzUyMH0; csrftoken=hUp8PA8F6FuVevk8RMpzujeerPI4Fuvd; shbid=12189; ds_user_id=1711504888; sessionid=1711504888%3A2mxQlbkxSvNRCW%3A10; rur=VLL; shbts=1584533496.250059; urlgen="{\\"93.188.37.225\\": 25521}:1jEXzS:89Y2WXPwPzjagzxuJdeDL9ZYRGY"',
}

params = (
    ('__a', '1'),
)

with open('followers_list.json', 'r') as f:
    data = json.load(f)

count = 0
for user in data:
    count += 1
    username = user['username']
    try:
        response = requests.get(
            f'https://www.instagram.com/{username}/?__a=1',
            headers=headers, params=params).json()
        user['about'] = response['graphql']['user']['biography']
        user['subscriptions'] = response['graphql']['user']['edge_follow'][
            'count']

    except json.decoder.JSONDecodeError:
        print('Request failed. Sleeping 60 seconds')
        time.sleep(60)

    with open('followers_data.csv', 'w') as f:
        fieldnames = data[0].keys()
        csv_data = csv.DictWriter(f, fieldnames=fieldnames)
        csv_data.writeheader()
        csv_data.writerows(data)
    time.sleep(3 if count % 10 != 0 else 5)

    print(f'{count} subscribers downloaded')

