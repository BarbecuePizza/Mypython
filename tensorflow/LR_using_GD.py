# -*- coding: UTF-8 -*-

'''
用梯度下降的优化方法解决线性回归问题
'''

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#构建数据
from numpy.core.tests.test_mem_overlap import xrange

points_num = 100
vectors = []
for i in xrange(points_num):
    x1 = np.random.normal(0.0,0.66)
    y1 = 0.1 * x1 + 0.2 + np.random.normal(0.0,0.04)
    vectors.append([x1,y1])

x_data = [v[0] for v in vectors]
y_data = [v[1] for v in vectors]

#图像1 ： 展示100个随机数据点

plt.plot(x_data, y_data, 'r*', label="Original data")
plt.title("Linear Regression using Gradient descent")
plt.legend()
plt.show()

#构建线性回归模型
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0 )) #初始化 Weight
b = tf.Variable(tf.zeros([1])) #初始化 偏差 Bias
y = W * x_data + b             #模型计算出来的y

#定义 loss function
#对 Tensor 的所有维度计算  （（y - y_data) ^ 2 )之和 / N
loss = tf.reduce_mean(tf.square(y - y_data))

#用梯度下降的优化器来优化我们的 loss function
optimizer = tf.train.GradientDescentOptimizer(0.5) #设置学习率 0.5
train = optimizer.minimize(loss)

#创建会话
sess = tf.Session()

#初始化数据流图中的所有变量
init = tf.global_variables_initializer()
sess.run(init)

#训练 20 步
for step in xrange(20):
    sess.run(train)
    print("Step=%d, Loss=%f, [Weight=%f Bias=%f]" % (step, sess.run(loss), sess.run(W), sess.run(b)))

#图像2 ： 绘制所有的点并绘制出最佳拟合的直线
plt.plot(x_data, y_data, 'r*', label="Original data")
plt.title("Linear Regression using Gradient descent")
plt.plot(x_data, sess.run(W) * x_data + sess.run(b), label="Fitted line")#拟合的线
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#关闭会话
sess.close()
