# # 字符串转换
# msg = "This is " + "a Message."
# print(msg)
# print(msg.title())
# print(msg.upper())
# print(msg.lower())
#
# # 数字乘方
# num = 3 ** 3
# print(num)
#
# # 数字拼接字符串必须使用str方法
# print("happy ".title() + str(num) + " birthday".title())
#
# # 除法有小数点
# print(num / 2)


#
# # 列表表示
# list = ["one", "two", "three", "four", "five", "six"]
#
# print(list)
# print(list[2])
#
# # 将索引指定为-1，可让Python返回最后一个列表元素
# print(list[-1])
# print(list[-2])
#
# # 列表增删改
#
# list.append("seven")
# print(list[-1])
# list.insert(2, "two after")
# print(list)
#
# # 列表元素删除
#
# del list[2]
# print("del直接删除且不再使用元素" + list.__str__())
#
# # pop从列表中取出并删除，返回删除的元素
# element = list.pop()
# print("删除并取出了最后一个元素值："+element)
# print("删除第一个元素："+list.pop(0))
# print(list)
#
# # 按值删除元素
# # remove()只删除第一个指定的值
# list.remove("two")
# print(list)
#
# # 列表排序
#
# listA = ["one", "two", "three", "four", "five", "six"]
#
# # sort()方法按字母从小到大排列，更改列表原始顺序
#
# listA.sort()
# print(listA)
# # 排序顺序按原来顺序取反
# listA.sort(reverse=True)
# print(listA)
#
# # sorted()排序规则与sort()方法一致，只是不更改原始数据
# print("显示的："+ sorted(listA).__str__())
# print("原始的：" + listA.__str__())
# print(sorted(listA, reverse=True))
#
# # reverse()方法列表反转
#
# listA.reverse()
# print("反转后的列表：" + listA.__str__())
#
# # 遍历列表
# listB = ["blue", "yellow", "green", "gray", "white", "black"]
# # 只要是缩进就在循环体里,冒号表示下一行是循环的第一行
# for element in listB:
#     print(element)
#     print(element.title())
# print(element)
