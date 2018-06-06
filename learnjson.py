# -*-coding:utf-8 -*-
#!/usr/local/bin/python3

import json

data = {'num':1002,'name':'xiaozhi'}
json_str=json.dumps(data)
print('python原始数据：',data)
print("json对象:",json_str)

data2 = json.loads(json_str)
print("data2['name']:",data2['name'])
print("data2['num']:",data2['num'])

print('successed!')