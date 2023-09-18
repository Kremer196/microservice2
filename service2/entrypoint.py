import requests
import sys
import os
import validators

page_url = sys.stdin.readline().strip()

if validators.url(page_url):
    SERVICE1_URL = os.getenv('SERVICE1')

    message = requests.get(page_url).text
    data = ["md5", message]

    response = requests.post(SERVICE1_URL, data="\n".join(data).encode("utf-8"))

    if response.status_code == 200:
        print(response.text)
    else:
        print("Service 1 not responding")
else:
    print("Please provide a valid URL")
