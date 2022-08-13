import json
import sys
import requests


def create(name):
    with open("config.json") as config:
        data = json.load(config)

    url = 'https://api.github.com/user/repos'
    headers = {"authorization": data['headers']['password']}
    body = {
        "name": name,
        "private": data['body']['private'],
    }

    resp = requests.post(headers=headers, url=url, json=body)
    answer = resp.json()
    try:
        print(f'created repository: {answer["name"]}')

    except:
        print(answer['message'])


def main():
    create(sys.argv[1])


if __name__ == "__main__":
    main()
