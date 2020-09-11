
字典：{} # 字典是以键值对的形式展现的
a = {"name":"张三","age":12} #{key：values}
print(a)
'''
字典的取值：
字典没有下标的概念，元祖数组有下标的概念，说明了字典没有顺序的说法
字典的取值靠key取值。
'''
print(a["age"]) 字典的取值 取key值

字典的新增：
a["adress"] = "成都" 当key不存在时就是新增
修改
当key存在时就是修改
a.update(name = "王二") # update的写法的时候，可以
在这里是一个变量的写法。


取值：
a["name"] #通过[]加上key去取值
a.get("name") # 通过get取值更加取值，当key不存在时，返回空值

取走

a.pop("name") # 取走key

#通用的删除方法，可以删字典也可以删数组

del a["name"] # 删除字典里面写key值，数组里面写下标

keys可以拿出来所有的key值，转换成数组

list(a.keys())
list(a.values())