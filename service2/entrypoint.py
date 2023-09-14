import requests
import sys
import os

SERVICE1_URL = os.getenv('SERVICE1')

message = requests.get(sys.stdin.readline()).text
data = ["md5", message]

response = requests.post(SERVICE1_URL, data="\n".join(data))

if response.status_code == 200:
    print(response.text)
else:
    print("Service 1 not responding")