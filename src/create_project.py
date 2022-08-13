import sys
import requests


class CreateRepository:
    def __init__(self, name):
        self._name = name
        self._make_repository()

    def _make_repository(self):
        url = 'https://api.github.com/user/repos'
        headers = {"authorization": "password"}
        body = {
            "name": self._name,
            "private": 'true',
        }

        resp = requests.post(headers=headers, url=url, json=body)
        answer = resp.json()
        try:
            print(f'created repository: {answer["name"]}')
        except:
            print(answer['message'])


def main():
    repository = CreateRepository(sys.argv[1])


if __name__ == "__main__":
    main()
