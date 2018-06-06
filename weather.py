# -*-coding:utf-8 -*-
#!/usr/local/bin/python3


# 继承 多态 封装 python类的用法

class WeatherSearch(object):
    """docstring for WeatherSearch"""

    def __init__(self, input_daytime):
        self.input_daytime = input_daytime

    def seach_visibility(self):
        visible_level = 0
        if self.input_daytime == 'daytime':
            visible_level = 2
        if self.input_daytime == 'night':
            visible_level = 9
        return visible_level

    def seach_temperature(self):
        temperature = 0
        if self.input_daytime == 'daytime':
            temperature = 26
        if self.input_daytime == 'night':
            temperature = 16
        return temperature


class OutAdvice(WeatherSearch):
    """docstring for OutAdvice"""

    def __init__(self, input_daytime):
        WeatherSearch.__init__(self, input_daytime)

    def seach_temperature(self):
        vehicle = ''
        if self.input_daytime == 'daytime':
            vehicle = 'bike'
        if self.input_daytime == 'night':
            vehicle = 'taxi'
        return vehicle

    def out_advice(self):
        visible_level = self.seach_visibility()
        if visible_level == 2:
            print('The weather is good,suitable for use %s.' % self.seach_temperature())
        elif visible_level == 9:
            print('The weather is bad,you should use %s.' % self.seach_temperature())
        else:
            print('The weather is beyond my scope,I can not give you any advice')


sth = input('请输入天气情况')
check = OutAdvice(sth)
check.out_advice()
