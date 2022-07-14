# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# # 导入模块并调用模块内方法
# import  daythree
#
# daythree.maxV(1,3,54,2,5,6,36,23,45)

# 导入模块中的某个函数，此时可直接使用导入的函数

from daytwo import min, min3 as minV

min(1, 2)
minV(2, 4, 2)