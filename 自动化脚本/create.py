# -*- coding: utf-8 -*-
import sys
import os
from github import Github

path = "/Users/wh_happy/常用/python/MyProjects/"

username = "BarbecuePizza"
password = "Shgjbmj-123"

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + folderName)
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Successfully created repository {}".format(sys.argv[1]))

if __name__ == "__main__":
    create()