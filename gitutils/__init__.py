import re
import pygit2
import sh
import os

sign_off_re = re.compile(r"^Signed-off-by: (.*)", flags=re.MULTILINE)

git = sh.Command("git")


def short_hash(commit):
    return git("rev-parse", "--short", commit.id).rstrip()


def get_current_branch(repo):
    if repo.head_is_detached:
        return None
    return repo.lookup_branch(repo.head.shorthand)


def get_repo(path):
    path = os.path.abspath(path)
    try:
        path = pygit2.discover_repository(path)
        os.chdir(path)
        return pygit2.Repository(path)
    except KeyError:
        print("Cannot find a repository in '{}'.".format(path))
        exit(1)
