# # 函数input()  输入的字符串，让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在 一个变量中，以方便你使用
# msg = input("input some word!")
# print(msg)
#
# # 函数int,将数字字符串转为数值类型
#
# a = "18"
# print(type(a))
# print(type(int(a)))
#
# # while 循环，可用break 和continue
# b = 1
# while b < int(a):
#     print(b ** 2)
#     b += 1
#     if b ** 2 > 256:
#         break
# print(b)

#  函数使用def声明

# def greet():
#     """文档注释符，用于生成文档时的函数注释"""
#     name = input("input your name\n")
#     print("Hello, " + name)
#
# greet()
#
# 函数传参
#
# def greet(name):
#     """文档注释符，用于生成文档时的函数注释"""
#     print("Hello, " + name + " ！")
#
# greet(input("input your name\n"))
#
# # 函数传递多个参数
#
# def greet(name1, name2):
#     print("Hello, " + name1+" and  " + name2 + " ！")
#
# greet("Liu", "Kong")
# greet(name2="Kong", name1="Liu")
#
# # 函数形参默认值
# def greet(name1, name2="Kong"):
#     print("Hello, " + name1+" and  " + name2 + " ！")
# greet("liu")
#
# # 函数返回结果
#
# def maxV(value1, value2=100):
#     if value1 > value2:
#         return value1
#     else:
#         return value2
#
# result = maxV(80)
# print(result)
#
# def split_name(first, secod="Lee"):
#     return first.title() + secod.title()
#
# while True:
#     first = input("input your first name\n")
#     second = input("input your second name\n")
#     print("hello, " + split_name(first, second))
#     print("\n")

# 使用星号传递任意数量的实参
# *value中的星号让Python创建一个名为value的空元组，并将收到的所有值都封装到这个元组中
def maxV(*value):
    print(value)


#
# maxV(1, 3, 5, 5, 6, 12, 3, 5, 32)
#
#
# # 使用两个星号创建空字典形参
# # 形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的所有名称—值对都封装到这个字典中
#
# def maxV2(max, **value):
#     print(max)
#     print(value)
#
#
# maxV2(3, location="beijing", lot="3321.32", lat="9283.293")
#
# # 定义类，类首字母大写，括号内空
#
# class Dog:
#     """模拟小狗类"""
#
#     # __init__()是一个特殊的方法，每当你根据Dog类创建新实 例时，Python都会自动运行它。
#     # 在这个方法的名称中，开头和末尾各有两个下划线，这是一种约 定，旨在避免Python默认方法与普通方法发生名称冲突
#     def __init__(self, name, age):
#         """初始化属性name 和age"""
#         self.name = name
#         self.age = age
#
#     # 每个与类相关联的方法 调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
#     # 以self为前缀的变量都可供类中的所有方法使用，我们 还可以通过类的任何实例来访问这些变量。
#     def sit(self):
#         """模拟小狗蹲下动作"""
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         """模拟小狗打滚动作"""
#         print(self.name.title() + " rolled over.")
#
#
# # 通常可以认为首字母大写的名称(如 Dog)指的是类，而小写的名称(如my_dog)指的是根据类创建的实例
# my_dog = Dog("rock", 18)
# print("my dog name is " + my_dog.name.title())
# my_dog.sit()


# 类内属性默认值，以及修改属性值

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.step_Numbers = 0

    def climb(self):
        print(self.name + " is climb up a tree")

    def eat(self):
        print(self.name + " is eating food.")

    def set_step_numbers(self, step):
        if step < self.step_Numbers:
            print("error! step numbers cant not roll back")
        else:
            self.step_Numbers = step


my_cat = Cat("Lucy", 2)
print("my cat name is " + my_cat.name.title())
print(my_cat.name.title() + " step_numbers is " + my_cat.step_Numbers.__str__())

# 直接修改属性值
my_cat.step_Numbers = 800
print(my_cat.name.title() + " step_numbers is " + my_cat.step_Numbers.__str__())
# 可以在类内定义方法修改属性值
my_cat.set_step_numbers(900)
print(my_cat.name.title() + " step_numbers is " + my_cat.step_Numbers.__str__())


# 继承
# 创建子类时，父类必须包含在当前文件中，且位于子类前面。 定义子类时，必须在括号内指定父类的名称
class Dragen_Li(Cat):
    """狸花猫类"""
    # 初始化时给父类的所有属性赋值
    def __init__(self, name, age):
        super().__init__(name, age)

    # 对于父类的方法，子类都可对其进行重写。为此，可在子 类中定义一个这样的方法，即它与要重写的父类方法同名。
    # 这样，Python将不会考虑这个父类方 法，而只关注你在子类中定义的相应方法
    def climb(self):
        print("Dragen_Li doesn't climb!")


my_dragen_li = Dragen_Li("Jack", 7)

my_dragen_li.climb()
my_dragen_li.eat()

