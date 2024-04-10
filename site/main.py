import os
from GUI import Interface

class Program:
    def __init__(self):
        Interface()

    def dependencies(self):
        os.system("pip install gitpython")
        os.system("pip install shutil")

    def clone(self):
        from git import Repo
        Repo.clone_from("repo.git", self.getCurrentDic())

    def getCurrentDic(self):
        return str(os.getcwd())

if __name__ == "__main__":
    program = Program()