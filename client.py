from helpers import get_from_config
from github import Github

class Client:
    def __init__(self):
        self.client = Github(get_from_config("GITHUB_KEY"))