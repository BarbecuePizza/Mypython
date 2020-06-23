#
# e1*s1+e2*s2 = 1 可求出s1、s2
# m = (c1^s1 * c2^s2)%n 已知c1、s1、c2、s2、n可求出m
#
import tkinter as tk
# 定义全局变量
e1 = e2 = n = m = c1 = c2 = s1 = s2 = M = ""

def attack():
	global e1, e2, n, m, c1, c2, s1, s2, M
	# 1. 获取变量传输进来的值
	e1 = int(var_e1.get())
	e2 = int(var_e2.get())
	n = int(var_n.get())
	m = int(var_m.get())

	# 2. 利用公钥对明文加密，得到密文c1、c2
	c1 = rsa(m, e1, n)
	c2 = rsa(m, e2, n)

	# 3. 根据公式e1*s1+e2*s2 = 1 求出该式子的一组解（s1,s2）
	g, s1, s2 = egcd(e1, e2)

	# 4. 求模反元素
	# 在数论模运算中，要求一个数的负数次幂，与常规方法并不一样。
	# ab=1(mod n) 这里b 就是a 的模反元素
	# 比如此处要求c1的s1次幂，就要先计算c1的模反元素c1r，然后求c1r的-s1次幂。
	if s1<0:
		s1 = -s1
		c1 = modinv(c1, n)
	elif s2<0:
		s2 = -s2
		c2 = modinv(c2, n)

	# 5. 根据公式 m = (c1^s1 * c2^s2)%n 求出明文m
	M = (c1**s1)*(c2**s2)%n
	print('M = ', M)
	c2 = rsa(m, e2, n)
	g, s1, s2 = egcd(e1, e2)
	value_place()

# 将得到的结果替换到GUI相应的位置
def value_place():
	global var_c1, var_c2, var_x, var_y, var_M

	var_c1.set(c1)
	_var_c1 = tk.Entry(window, textvariable=var_c1, width=15, state = 'disabled')
	_var_c1.place(x=390, y=107)

	var_c2.set(c2)
	_var_c2 = tk.Entry(window, textvariable=var_c2, width=15, state = 'disabled')
	_var_c2.place(x=390, y=142)

	var_x.set(s1)
	_var_x = tk.Entry(window, textvariable=var_x, width=10, state = 'disabled')
	_var_x.place(x=60, y=246)

	var_y.set(s2)
	_var_y = tk.Entry(window, textvariable=var_y, width=10, state = 'disabled')
	_var_y.place(x=250, y=246)

	var_M.set(M)
	_var_M = tk.Entry(window, textvariable=var_M, width=15, state = 'disabled')
	_var_M.place(x=435, y=405)

# RSA加密算法
def rsa(M, e, n):
  return (M**e)%n


def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


def modinv(a, m):
  g, x, y = egcd(a, m)
  if g != 1:
    raise Exception('modular inverse does not exist')
  else:
    return x % m


# 定义GUI主体框架
window = tk.Tk()
window.title('RSA 共模攻击')
window.geometry('600x500')

# 定义输入变量
var_e1 = tk.StringVar()
var_e2 = tk.StringVar()
var_n = tk.StringVar()
var_M = tk.StringVar()
var_c1 = tk.StringVar()
var_c2 = tk.StringVar()
var_x = tk.StringVar()
var_y = tk.StringVar()
var_m = tk.StringVar()

# 设置画布
tk.Label(window, text='e1 = ', font=('Arial', 30)).place(x=10, y= 20)
tk.Label(window, text='e2 = ', font=('Arial', 30)).place(x=200, y= 20)
tk.Label(window, text='n = ', font=('Arial', 30)).place(x=400, y= 20)
tk.Label(window, text='M  = ', font=('Arial', 30)).place(x=10, y= 60)
tk.Label(window, text='C1 = M^e1(mod n) = ', font=('Arial', 30)).place(x=100, y= 100)
tk.Label(window, text='C2 = M^e2(mod n) = ', font=('Arial', 30)).place(x=100, y= 135)
tk.Label(window, text='-'*58, font=('Arial', 30)).place(x=10, y= 200)

tk.Label(window, text='x = ', font=('Arial', 30)).place(x=10, y= 240)
tk.Label(window, text='y = ', font=('Arial', 30)).place(x=200, y= 240)
tk.Label(window, text='e1*x + e2*y = 1', font=('Arial', 30)).place(x=360, y= 240)
tk.Label(window, text='M = M^(e1*x + e2*y)', font=('Arial', 30)).place(x=100, y= 300)
tk.Label(window, text='= (M^e1)^x * (M^e2)^y', font=('Arial', 30)).place(x=135, y= 350)
tk.Label(window, text='= c1^x*c2^y(mod n) = ', font=('Arial', 30)).place(x=135, y= 400)

# 设置输入框的位置
var_e1 = tk.Entry(window, textvariable=var_e1, width=10)
var_e1.place(x=80, y=27)

var_e2 = tk.Entry(window, textvariable=var_e2, width=10)
var_e2.place(x=270, y=27)

var_n = tk.Entry(window, textvariable=var_n, width=12)
var_n.place(x=455, y=27)

var_m = tk.Entry(window, textvariable=var_m, width=15)
var_m.place(x=80, y=67)


# 定义botton
btn_login = tk.Button(window, text='ATTACK', command=attack)
btn_login.place(x=450, y=190)
window.mainloop()


