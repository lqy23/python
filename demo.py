# # print("您好啊，巧云")

# # python的常见方法：
# # print（） 打印输出

# # python的数据类型：
# # 字符串、整数、小数（浮点型数据）、布尔值、空、元祖、数组、字典

# # print(234) 整数
# # print(2.3) 小数
# # print(True,False) 布尔值
# # print(None) 空
# # print(()) 元祖
# # print([]) 数组
# # print({}) 字典
# # print里面可以写很多的数据，用，隔开


# # print控制换行的方法，end

# print("您好啊，巧云" ,end="") #end里面没有写内容默认以换行结尾，写内容了就紧跟其后。
# print("哈哈",2333,"您好啊")

# # 字符串相加是拼接的效果
# print("哈哈"+"希希") # 字符串是可以相加的 ，减号除号是不可以的
# print("哈哈"*10) # 相乘，出来10 个哈哈

# # 整数和小数都可以实现正常的数学运算

# print(1+2.3)

# # 不同的数据类型不可以做操作，只能同类型做操作 

# # python的运算符 + — * / %  //取整
# print(10%3) # 余1
# print(10//3) # 取整 3 

# # 布尔值 True/1 False/0 对和错的意思
# print (1>3) # 出来结果False

# # python的判断符号：> 、< 、== 、!=、in、is

# # py的逻辑连接符：and、or

# print(1 == 2 or 1 < 3)

# # python的重要概念
# # 变量： 
# name ="张三"
# print(name )
# # 把张三这个值赋值给了name这个变量

# # input 获取输入
# a = input("请输入：")
# print("这是我刚刚输入的值：",a)

# # 作业：分别输入2个数字，并计算他们的和
# a = input("请输入第一个数字")
# b = input("请输入第二个数字")
# # 任何通过input获取到的值都是字符串类型

# print("这是他们的和：",a + b) 

# # type() 获取到数据的类型
b = type("hahaha")
print(b)

# 类型英文：字符串/str,整数/int，小数/float,布尔值/bool,空/NoneType，元祖/tuple,数组/list,字典/dict

# 转换数据类型方法：str、int、float、bool、tuple、list、dict
# a = str(2333) # 数字转换成字符串类型
# print(type(a))

# a = tuple[1,2,3]
# print(type(a))


# 数据类型转换规律：任何数据都可以转换成字符串
# 字符串转换成数字或者小数要满足长得像这个规律 

# 字符串可以转换成元祖和数组，元祖和数组可以相互转换。


# a = (1,2,3)
# print(type(a)) 

# len() 或许数据的长度，数字，布尔值、空没有长度
a = len("哈哈哈哈")
print(a)

# 作业：请实现一个计算字数是单数还是双数的程序，
print("0:表示偶数；1：表示奇数：")
a = input("请输入一个数字：")
print(len(a)%2)

