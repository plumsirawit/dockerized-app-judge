import git
from pathlib import Path
import shutil

dirpath = Path('./__submission')
def clone(url):
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

    # TODO: test for validity of url

    git.Git(str(dirpath.resolve())).clone(url)