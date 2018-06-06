# -*-coding:utf-8 -*-
#!/usr/local/bin/python3

class Student(object):
    """docstring for Stedent"""

    def __init__(self, name, score):

        self.__name = name
        self.__score = score

    def info(self):
        print('学生：%s; 分数:%s' % (self.__name, self.__score))

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print('请输入0到100的数字。')


# set用来避免传入无效的参数

stu = Student('xiaoming', 95)
print('修改前分数:', stu.get_score())
stu.info()
stu.set_score(122)
print('修改后分数:', stu.get_score())
stu.info()
