# if True:
#     print("True")
# else:
#     print("False")
#     #无缩进行执行报错
#     print("aaaaa")

# word = 'world'
# print(word)
#
# text = "你哈大大大噶蛋糕大哥啊"
# print(text)
#
# texts = """    你好
#  你啊好伐毮的啊"""
# print(texts)

# a = 1
# if a < 0:
#     print("a小于0")
# elif a == 0:
#     print("a等于0")
# else:
#     print("a大于0")
# a = input("请输入a的值：")
# print(a)
# intStr = 1
# floatStr = 1000.1
# stringStr = "a"
#
# print(intStr)
# print(floatStr)
# print(stringStr)

# a, b, c = 1, 2.0, "1111"
# print(a, b, c)
# a = "1"
#
# if a.__eq__("1") and a.__eq__("2"):
#     print("1")
# else:
#     print("2")

# list = [123, 10.5, 'a', 'c']
#
# print(list)
#
# print(list[1])
#
# print(list[1:3])
#
# print(list[1:])
#
# print(list * 2)
#
# print(list + list)
# # 元组不允许更新赋值
# tuple = (134, 10.4, '1111', 'aaaa')
#
# print(tuple)

# dictionary = {};
#
# dictionary['name'] = "leo"
#
# dictionary['age'] = 26
#
# print(dictionary)
#
# dict = {"name": "leo", "age": 26}
#
# print(dict)
#
# print(dict.keys())
#
# print(dict.values())
#
# print(dict.get("name"))
#
# print(dict.__sizeof__())

# sets = {"leo", "zzw", "spf", "zzj"}
#
# print(sets)
#
# if 'leo' in sets:
#     print("leo 在set中")
# else:
#     print("leo 不在set中")
#
# a = set("abcd")
# b = set("bcdef")
#
# print(a | b)
#
# print(a - b)
#
# print(b - a)
#
# print(a & b)
#
# print(a ^ b)

# x = 1
#
# b = int(x)
#
# print(b)
#
# y = "111.1"
#
# print(y)
#
# a = float(y)
#
# print(a)
#
# print(bool(x))
#
# p = ("a", "b")
#
# print(dict(p))


# a = 'a b c d'
#
# print(list(a))
#
# print(isinstance(a, int))


# class A:
#     def __eq__(self, o: object) -> bool:
#         if isinstance(self, object):
#             return True
#         return super().__eq__(o)
#
#
# class B(A):
#     pass


#
# print(isinstance(A(), A))
#
# print(isinstance(B(), A))  # isinstance 会认为子类是父类的类型
#
# print(type(A()) == A)
#
# print(type(B()) == A)  # type 不会认为 子类是父类的类型
# a = A()
#
# b = a
# print(id(a) == id(b))
#
# print(a is b)



import math

a = 3
b = 2

c = min(b, a)

d = abs(a)
print(c)
print(d)

f = math.pow(a, b)
print(f)
