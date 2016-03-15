import si301.email
import si301.utils

class Author:

    def __init__(self, name):
        self.contributions = {}
        self.set_name(name)

    def add_contribution(self, project, n=1):
        """ Add n contribution(s) from this author to the given project """
        try:
            self.contributions[project] = self.contributions[project] + n
        except KeyError:
            self.contributions[project] = n

    def set_name(self, name):
        """ Parses strings like "Alec Ten Harmsel <talec@umich.edu>" """
        parts = name.split("<")
        if len(parts) != 2:
            raise ValueError("I don't know how to parse " + name)

        self.fullname = parts[0].rstrip()
        self.email = si301.email.Address(parts[1])


class Commit:

    def __init__(self, path_to_repo, revision):
        raw = si301.utils.cd_cmd(path_to_repo,
                ["git", "show", "--format=short", revision])

        for line in raw.split("\n"):
            if len(line) > 0 and line.startswith("Author: "):
                self.author = line.replace("Author: ", "")


class Repo:

    def __init__(self, path):
        self.path = path
        self.rev_list = []

    def rev_list(self):
        if len(self.rev_list) == 0:
            raw = si301.utils.cd_cmd(self.path_to_repo,
                    ["git", "rev-list", "--reverse", "HEAD"])
            self.rev_list = raw.split("\n")

        return self.rev_list
