import requests
import subprocess
from time import sleep

headers = {
    'Host': '10.254.0.253:8080',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept': '/',
    'Connection': 'close',
    'X-Team-Token': 'e5902a784c4ca765',
    # 'Content-Length': '36',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
}

json_data = [
    'PMYI4B847OF06GHRUJVMP3EEXX2VXMK=',
]
while True:
    try:    
        response = requests.put('http://10.254.0.253:8080/flags', headers=headers, json=json_data, verify=False)
        print(response.text)
    except:
        print('error')