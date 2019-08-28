# python变量类型和运算符

# -*-coding:utf-8-*-

# python 单行注释
'''
python 多行注释
'''


# pyhton变量命名必须是大小写的英文字母、数字、下划线（_）的组合，不能以数字开头
# python的变量类型及其运算符
# 变量：“盛装”程序中的数据，变量保存的数据可以多次发生改变，只要程序对变量重新赋值即可
# 常量：常量保存的数据不可以发生改变


'''
# 强类型语言：C，C++，java
# 弱类型语言 ：python
弱类型语言的特征：
（1）变量无须声明即可赋值，对一个不存在的变量赋值就相当于定义了一个新的变量
（2）变量的数据类型可以动态改变：同一个变量可以一会儿被赋值为整数值，一会儿被赋值为字符串
a = 5
'''
a = 5
print(type(a))  # ype()输出传入数据的类型
a = "hello "
print(type(a))

# 数值类型 不可变 python修改数值类型变量的值，其实只是修改变量名所表示的内存空间
# 数值类型： 整形、 浮点型、 复数类型
'''
整形：正整数、负整数、0
java： 根据数值大小 选择 short、int、long
python中整形支持存储各种整数值，无论多大或者多小，pyhton都能轻松处理
python的整形支持None值
        a = None 
        print(a)  #输出None
python3.X支持数值（包括浮点型）增加下划线作为分隔符，这些下划线不会影响数值本身的大小
'''
name = "weizhi"
age = 20
print("姓名", name ,"性别",age,sep="|")
print("姓名", name ,"性别",age)