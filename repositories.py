from client import Client

class Repositories:
    def __init__(self):
        self.client = Client()

    def list_personal_repositories(self):
        return self.client.client.get_user().get_repos("all", "owner")

    def list_explorer_repositories(self):
        repositories = self.list_personal_repositories()
        explorer_repositories = []
        for repository in repositories:
            if repository.full_name.endswith('_explorer'):
                explorer_repositories.append(repository)
        return explorer_repositories

    def list_core_repositories(self):
        repositories = self.list_personal_repositories()
        core_repositories = []
        for repository in repositories:
            if repository.full_name.endswith('_core'):
                core_repositories.append(repository)
        return core_repositories

    def delete_repositories(self):
        repositories = self.list_explorer_repositories() + self.list_core_repositories()
        print("The following list of repositories will be deleted.")
        print(repositories)
        for repository in repositories:
            repository.delete()
        print("Successfully removed your core and explorer repositories.")