
# range()函数创建数字列表
# listC = list(range(2, 11, 2))
# print(listC.__str__())
#
# listD = []
# for num in range(2, 11, 2):
#     listD.append(num ** 2)
# print(listD.__str__())
# # 数字列表计算
# print("min: " + str(min(listD)) + "  max:" + str(max(listD)) + "  sum:" + str(sum(listD)))
#
# 列表解析
"""
首先指定一个描述性的列表名，如squares;然后，指定一个左方括号， 并定义一个表达式，用于生成你要存储到列表中的值。
在这个示例中，表达式为value**2，它计算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。
请注意，这里的for 语句末尾没有冒号
"""
# squares = [value ** 2 for value in range(2, 11, 2)]
# print(squares)
#
# # 列表切片
# # 后一个索引不包含
# print(squares[1:3])
#
# print(squares[1:])
# print(squares[:3])
# print("最后两个：" + squares[-2:].__str__())
#
# # 列表复制，值复制，区别于直接等号赋值是变量指向
#
# food = ["pizza", "rice", "Dumplings", "hamburger", "noodle"]
#
# eat = food[:]
# eat.append("steak")
# print(eat)
#
# # 不可变的列表被称为元组
#
# listD = (1, 2, 3, 4, 5)
# print(listD)
# # listD[1] = 7 会报错
# # 虽然不能修改元组的元素，但可以给存储元组的变量赋值
# listD = (2, 3, 4)
# print(listD)
#
# if语句
#
# list = ["one", "two", "three", "four", "five", "six"]
#
# for element in list:
#     # if element == "four":
#     #     print(element.upper())
#     # else:
#     #     print(element.title())
#     if element != "five" and element != "six":
#         print(element.lower())
#     else:
#         print(element.upper())
#
# if 3 == 6 or 7 >= 2:
#     print("True")
# else:
#     print("false")
#
# in关键字表示是否在列表中
# listA = ["one", "two", "three", "four", "five", "six"]
# print("one" in listA)
# print("size" not in listA)
#
# # 多重选择语句
#
# age = 30
#
# if age < 18:
#     print("未成年")
# elif age < 30:
#     print("青年")
# elif age < 60:
#     print("中年")
# else:
#     print("退休了吧")
#
# # 字典字典用放在花括号{}中的一系列键—值对表示，没有顺序
#
# map = {"color": "green", "size": "13", "content": "字典"}
# print(map["color"])
#
# # 字典内添加值
# print(map)
# map["bg_color"] = "red"
# print(map)
#
# # 删除键值对
# del map["size"]
# print(map)
#
# # 多行字典
#
# favorite_language = {
#     "Li": "Kotlin",
#     "Liu": "OC",
#     "Zhang": "Java",
#     "Kong": "Flutter",
#     "yang": "OC"
# }
# print(favorite_language)
#
# # 字典遍历
#
# for key, value in favorite_language.items():
#     print(key+", " + value)
#
# # 键遍历
#
# for key in favorite_language.keys():
#     print(key)
#
# # 字典默认遍历键
# for key in favorite_language:
#     print(key)
#
# # 值遍历
# # 遍历值，并按顺序排列
# for v in sorted(favorite_language.values()):
#     print(v)
#
# # set函数去重
# for v in set(favorite_language.values()):
#     print(v)
#
# # 列表中嵌套字典
#
# listA = []
# for i in range(10):
#     listA.append({"name": "Li" + str(i), "No": i, "age": i ** 2 + 10})
# for element in listA:
#     print(element)
# print("\n")
#
# # 字典中嵌套列表
#
# listB = [1, 3, 5, 7, 9]
# listC = {"one": "two"}
#
# map = {"number": listB, "numE": listC}
# print(map)

def min(v1, v2):
    print(v1)
    print(v2)

def min2(v1, v2, v3):
    print(v1)
    print(v2)
    print(v3)

def min3(*v):
    print(v)