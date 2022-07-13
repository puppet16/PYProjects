
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

# 列表解析
"""
首先指定一个描述性的列表名，如squares;然后，指定一个左方括号， 并定义一个表达式，用于生成你要存储到列表中的值。
在这个示例中，表达式为value**2，它计算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。
请注意，这里的for 语句末尾没有冒号
"""
squares = [value ** 2 for value in range(2, 11, 2)]
print(squares)
