# -*-coding:utf-8 -*-
#!/usr/local/bin/python3

def first_recurring(given_string):
    counts = {}  # dictionary or hash table
    for char in given_string:
        if char in counts:
            print(char)
        else:
            counts[char] = 1
    return None

given_string = input("请输入字符串")
first_recurring(given_string)
