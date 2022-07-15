# # 文件操作
# # open 函数打开入参文件名的文件，并返回该文件对象
# # 文件名使用的相对路径，即本文件所在目录
# # 关键字with在不再需要访问文件后将其关闭
# with open("pi_digits.txt") as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())
#

# 逐行读取
# 在这个文件中，每行的末尾都有一个看不见的换行符，而 print语句也会加上一个换行符，因此每行末尾都有两个换行符:一个来自文件，另一个来自print 语句
# file_name = "pi_digits.txt"
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# 创建读取每行的一个列表

file_name = "pi_digits.txt"
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_str =''
for line in lines:
    print(line.rstrip())
    pi_str += line.strip()

print(pi_str)
print("length：" + len(pi_str).__str__())
print("输出pi小数点后10位：" + pi_str[:12].__str__())












