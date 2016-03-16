import os
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
        self.email = si301.email.Address(parts[1].replace(">", ""))


class Commit:

    def __init__(self, path_to_repo, revision):
        if len(revision) == 0:
            raise ValueError("Invalid revision " + revision)

        raw = si301.utils.cd_cmd(path_to_repo,
                ["git", "show", "--format=short", revision])

        for line in raw.split("\n"):
            if len(line) > 0 and line.startswith("Author: "):
                self.author = Author(line.replace("Author: ", ""))


class Repo:

    def __init__(self, path):
        self.path = path
        self.revs = []
        self.project = os.path.split(path)[-1]

    def rev_list(self):
        if len(self.revs) == 0:
            raw = si301.utils.cd_cmd(self.path,
                    ["git", "rev-list", "--reverse", "HEAD"])
            self.revs = raw.split("\n")

        return self.revs

    def get_authors(self):
        authors = {}

        for rev in self.rev_list():
            commit = None

            try:
                commit = Commit(self.path, rev)
            except ValueError:
                continue

            auth = commit.author

            try:
                authors[str(auth.email)].add_contribution(self.project)
            except KeyError:
                authors[str(auth.email)] = auth
                authors[str(auth.email)].add_contribution(self.project)

        l = []
        for auth in authors:
            l = l + [authors[auth]]

        return l
