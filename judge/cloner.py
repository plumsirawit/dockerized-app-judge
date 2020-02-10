import git
from git.exc import GitCommandError
from pathlib import Path
from os import mkdir
import shutil

dirpath = Path('./__submission')
def clone(url):
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

    mkdir(str(dirpath))

    try:
        git.Git(str(dirpath.resolve())).clone(url, ['--recursive','.'])
    except GitCommandError:
        return 400