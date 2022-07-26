# file_name = "pi_million_digits.txt"
#
# with open(file_name) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ""
# for line in lines:
#     pi_string += line.strip()
#
# # print(pi_string[:52] + "...")
# # print(len(pi_string))
#
# birthday = input("Enter your birthday, in the form yymmdd:\n")
#
# if birthday in pi_string:
#     birthdayIndex = pi_string.index(birthday)
#     print(birthdayIndex)
#     print(pi_string[birthdayIndex - 2: birthdayIndex + len(birthday)])
#     print("appear")
# else:
#     print("do not")

# 写入文件
# 调用open()时提供了两个实参。第一个实参也是要打开的文件的名称; 第二个实参告诉Python，我们要以何种模式打开这个文件。
# 打开文件时，可指定读取模 式('r')、写入模式('w')、附加模式('a')或让你能够读取和写入文件的模式('r+')。
# 如果 你省略了模式实参，Python将以默认的只读模式打开文件。
# 如果你要写入的文件不存在，函数open()将自动创建它。
# 以写入('w')模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件
#
# file_name = "programing.txt"
# # with open(file_name, 'w') as file_object:
# #     file_object.write("I LOVE YOU.\n")
# #     file_object.write("HOPE YOU TOO")
#
# # 附加模式即在文件末尾添加内容，不会先清空文件
#
# with open(file_name, "a") as file_object:
#     file_object.write("\nSure")
#
# # 异常捕获
#
# try:
#     print(5/ 0)
# except ZeroDivisionError:
#     print("Your can't divide by zero!")
#
# # 异常捕获之else
# # 依赖于try代码块成功执行的代码都应放到else代码块中
# try:
#     print(5/ 0)
# except ZeroDivisionError:
#     print("Your can't divide by zero!")
# else:
#     print("执行成功")

# 打印某文件里单词使用次数最多的前一百个
file_name = "The Count of Monte Cristo.txt"
try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileExistsError:
    print("Sorry, file not found!")
else:
    words = contents.split()
    num_words = len(words)
    print("file has about " + num_words.__str__() + " words")

    map = {}
    for word in words:
        if not word.isalpha():
            continue
        if word in map.keys():
            map[word] = map[word] + 1
        else:
            map[word] = 1
    map2 = sorted(map.items(), key=lambda x:x[1], reverse=True)
    print(map2[:100])
