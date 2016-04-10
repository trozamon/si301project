import os
import re
import si301.email
import si301.utils

class Author:

    def __init__(self, name):
        self.contributions = 0
        self.set_name(name)

    def add_contribution(self, n=1):
        """ Add n contribution(s) from this author to the given project """
        self.contributions = self.contributions + n

    def set_name(self, name):
        """ Parses strings like "Alec Ten Harmsel <talec@umich.edu>" """
        parts = name.split("<")
        if len(parts) != 2:
            raise ValueError("I don't know how to parse " + name)

        self.fullname = parts[0].rstrip()
        self.email = si301.email.Address(parts[1].replace(">", ""))


class CommitMessage:

    def __init__(self, raw_msg):
        for line in raw_msg.split("\n"):
            if len(line) > 0 and line.startswith("Author: "):
                self.author = Author(line.replace("Author: ", ""))


class Commit:

    def __init__(self, path_to_repo, revision):
        if len(revision) == 0:
            raise ValueError("Invalid revision " + revision)

        raw = si301.utils.cd_cmd(path_to_repo,
                ["git", "show", "--format=short", revision])

        self.msg = CommitMessage(raw)


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

    def get_log(self):
        return si301.utils.cd_cmd(self.path, ['git', 'log'])

    def get_authors(self):
        authors = {}

        for rev in self.rev_list():
            commit = None

            try:
                commit = Commit(self.path, rev)
            except ValueError:
                continue

            auth = commit.msg.author

            try:
                authors[str(auth.email)] = authors[str(auth.email)] + 1
            except KeyError:
                authors[str(auth.email)] = 0

        return authors

    def get_authors_fast(self):
        raw_log = self.get_log().split("\n")
        regex = re.compile('^Author: .* <.*>$')
        authors = {}

        for line in raw_log:
            if regex.match(line):
                auth = Author(line.replace("Author: ", ""))

                try:
                    authors[str(auth.email)] = authors[str(auth.email)] + 1
                except KeyError:
                    authors[str(auth.email)] = 1

        return authors

    def tag_list(self):
        return si301.utils.cd_cmd(self.path, ['git', 'tag', '-l']).split("\n")

    def get_tag_dates(self):
        msgs = si301.utils.cd_cmd(self.path, ['git', 'show', '--tags'])
        date_strs = []

        for msg in msgs.split("\n"):
            if re.match('Date:.*\d+ \d+:\d+:\d+ \d\d\d\d [+-]\d\d\d\d', msg):
                date_strs.append(msg)

        return date_strs

    def get_tag_msgs(self):
        msgs = []

        for t in self.tag_list():
            if len(t) == 0:
                continue

            msgs.append(si301.utils.cd_cmd(self.path, ['git', 'show', t]))

        return msgs
