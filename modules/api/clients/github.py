import requests


class GitHub:
    def send_first_request(self):
        r = requests.get("https://api.github.com/zen")

        return r

    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name})
        body = r.json()

        return body

    def get_status_code(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        code = r.status_code

        return code

    def get_headers(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        header = r.headers

        return header
