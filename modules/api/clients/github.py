import requests


class GitHub:
    """This class describes requests from the GitHub documentation API."""

    def send_first_request(self):
        """This method sends an http request to the GitHub server and displays
        the response on the screen."""
        r = requests.get("https://api.github.com/zen")

        return r

    def get_user(self, username):
        """This method saves the body of the response in the body variable."""
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        """A method for searching a repository, where 'q' is the name of
        the searched repository."""
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name})
        body = r.json()

        return body

    def get_status_code(self, username):
        """This method saves the status code of the response in the code
        variable."""
        r = requests.get(f"https://api.github.com/users/{username}")
        code = r.status_code

        return code

    def get_headers(self, username):
        """This method saves the headers of the response in the
        header variable."""
        r = requests.get(f"https://api.github.com/users/{username}")
        header = r.headers

        return header
