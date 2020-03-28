# python变量类型和运算符

# -*-coding:utf-8-*-

# a = 5
# print(type(a))  # type()输出传入数据的类型
# a = "hello "
# print(type(a))

# print函数
# name = "weizhi"
# age = 20
# print("姓名", name ,"性别",age,sep="|")  # 改变默认的分隔符
# print("姓名", name ,"性别",age)

# print(40,"\t",end="")  # print默认换行（end="\n"），输出不换行修改end的值
# print(50,"\t",end="")
# print(60,"\t",end="\n")

# f = open("1.txt",'r+',encoding="utf-8")
# print("海上生明月",file = f)
# print("天涯共此时",file = f)
# print(f.read())
# f.close()

#复数
# s = 3 + 1j
# print(type(s)) # int 

# msg = input("请输入一个值：")
# print(type(msg))
# # print(msg)

# s1 = ["helo",90,"world"]
# s2 = ["1","20",30]
# print(s1 + s2)

# a_range = range(5)
# print(list(a_range)) # list()转换为列表
# print(tuple(a_range)) #tuple()转换为元组

# c_list = list(range(1,5))
# print(c_list)
# c_list.insert(3,"hello")
# print(c_list)
# c_list.insert(3,tuple("hello"))
# print(c_list)
# a = "hello"
# print(tuple(a))
# print(list(a))

# b_list = list(range(1,10))
# print(b_list)
# del b_list[2:-2:2]
# print(b_list)
# del b_list[2:4]
# print(b_list)

d_dict = {(20,30):'good',30:'bad'}
print(d_dict)