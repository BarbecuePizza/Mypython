#!/bin/bash

# 自动创建github仓库 
# made by wanghua 2019-8-25

function create() {
    cd /Users/wh_happy/常用/python/自动化脚本
    python3 create.py $1
    cd /Users/wh_happy/常用/python/MyProjects/$1 
    git init
    git remote add origin https://github.com/BarbecuePizza/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master

}

