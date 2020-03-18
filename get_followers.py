import json
import requests
import time

x_csrftoken = ''
account_name = ''
query_hash = ''

headers = {
    'authority': 'www.instagram.com',
    'x-ig-www-claim': 'hmac.AR2_weROM_I8a0gRuL-U_ugAvg5x-6P9tOW7a5eympVWYUpy',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-dest': 'empty',
    'x-requested-with': 'XMLHttpRequest',
    'x-csrftoken': x_csrftoken,
    'x-ig-app-id': '936619743392459',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': f'https://www.instagram.com/{account_name}/followers/?hl=ru',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
    'cookie': 'mid=W0S8nQAEAAGgkxjmeT_Ay7SjESHR; mcd=3; fbm_124024574287414=base_domain=.instagram.com; ig_did=D4B7081B-405D-4CAC-8E16-3C007DF1F2EC; fbsr_124024574287414=0hG9pveZtZ-5xJ83EE3WFcabRBSAc30_A6qrBEs6eBs.eyJ1c2VyX2lkIjoiMTAwMDAxMjg0NDM0MDcxIiwiY29kZSI6IkFRQVdQcEdjWm5pc0M3SUR4Ym9yWW5BRzFwa2plRFpFU1BGYlItMzB4SWNGQ2xDa3QxV1NvV0VQbjc0aEMzdF90Mkx2eDVNeV9Od3p4dk11NGtJOTBPeEtaNk1uMUt3SDN6Z200MWdxNkt4eDVCWWxZZ1FBekRIU1VZTGpYOURnWWR4MkNHT20yYVcxRVdqNUFyUnE1SGo0UnMwMXVPM2p2T1Zta0pTVHBLWjl6N0VJWTRlRWt0UVdGWGNsLTg3RVhZUE1ZODBZZXhnLWl3T2hHVGxUWDVzSzF1MDJuQWZleklTNy1BbGhGVTdxbXl4T0ppcWFVczMxbHV4V3JONXppZ1cxYmhnY0NFSDA5aWxmRl9FblNSZXhxRWFRYVhOcVROUmxNWF96RUV5cXZrV0hLd1hJYnZ1dGlWcWVSaUVVdDZaN003Ml9yaTlGQWt6bGhuaFRqUzVYIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUV0djdKeW5aQUpQWkJLY1V3d2xReTFDVVpCb2dHM0daQXVyMzdSZTBvNlBBN2F0VFpDWHBSQjBKRDFCRXZJNTVUWHdta3I2cUxPR3RmUkJ5SVRsWkM2RXp2NHZGZTY2R29mY0lMeUJIbGI1T2Q5SkxhdzZFYVNIVVpDV2xZWkNiQ1pBSG1GR1VveGJqOXVsQjl4eGNub2pqczgxcFIxZWptakRiY012N1BGelQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTU4NDI3MzUyMH0; csrftoken=hUp8PA8F6FuVevk8RMpzujeerPI4Fuvd; shbid=12189; shbts=1584273521.6344442; ds_user_id=1711504888; sessionid=1711504888%3A2mxQlbkxSvNRCW%3A10; rur=VLL; urlgen="{\\"93.188.37.225\\": 25521}:1jDVFc:8mizLpE5fcMk3iiJB62tczcPFak"',
}

has_next_page = True
index = 0
after = None

while has_next_page:
    index += 1
    after = f',"after":"{after}"' if after else ''
    variables = f'{{"id":"1711504888","include_reel":true,"fetch_mutual":false,"first":20{after}}}'
    params = {
        'query_hash': query_hash,
        'variables': variables
    }
    response = requests.get('https://www.instagram.com/graphql/query/',
                            headers=headers, params=params)

    after = response.json()['data']['user']['edge_followed_by']['page_info']['end_cursor']

    has_next_page = response.json()['data']['user']['edge_followed_by']['page_info']['has_next_page']

    with open(f'followers/followers_{index}.json', 'w') as f:
        json.dump(response.json(), f, indent=4)

    time.sleep(5 if index != 0 else 20)