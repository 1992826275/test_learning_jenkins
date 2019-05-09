# -*- coding:utf8 -*-
# **********************************************
#    2019/4/30
#    BY  City_Bro
# **********************************************
'''
1.函数有哪几种参数类型，分别有什么特点？
'''
# 答】
# 必要参数
# 默认参数
# 不定长参数

# ************************************************************************************************************
'''
2.在函数调用时，位置参数和关键字参数的顺序
'''
# 答】
# 位置参数前
# 关键字参数后
# ************************************************************************************************************
'''
3、编写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
'''
# 答】
# def judge_len5(a):
#     if len(a) > 5:
#         print("长度大于5")
#     else:
#         print("长度小于5")

# ************************************************************************************************************
'''
4、编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
'''
# 答】
# def judge_len2(a):
#     if len(a) > 2:
#         print("大于两位")
#         return a[0:2]
#     else:
#         return a
# print(judge_len2([0,2]))

# ************************************************************************************************************
'''
5、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典
'''
# 答】
# def check_add(a,b):
#     value_list = []
#     b = str(b)
#     for i in a:
#         value_list.append(a[i])
#     if b in value_list:
#         print("字符串存在于该字典！")
#     else:
#         a[b] = b
#     print(a)
# check_add({'1':'1','2':'2','3':'3'},4)

# ************************************************************************************************************
'''
6、通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
'''
# 答】
# def algorithm(a,b):
#     order = int(input("请选择运算算法：加法【1】、减法【2】、乘法【3】、除法【4】"))
#     if order == 1:
#         return a+b
#     elif order == 2:
#         return a-b
#     elif order == 3:
#         return a*b
#     elif order == 4:
#         return a/b
#     else:
#         print("无法识别指令！")
# print(algorithm(7,8))
# ************************************************************************************************************
'''
7、一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
'''
# ************************************************************************************************************
'''
8、将上次作业的图书管理系统改成函数版本，每个功能封装成一个函数，原来功能上扩展，启动程序首先提示功能选项：
【1】登录，【2】注册，完成注册功能
main()：控制整个程序的运行流程                   
print_muen():打印菜单
login(): 登录功能                                             register：注册功能  
add_book():添加图书                                      del_book():删除图书
all_book():显示所有图书                                  find_book: 查找图书
update_book():修改图书
修复bug（扩展，不要求提交到作业）：
添加图书时，图书的id不能重复，图书名可以重复；
删除查询修改的时候，输入图书名之后提供所有同名的图书，给用户选择，用户可以选择其中的一本进行操作。
'''
# 用户账号信息列表
user_info = [{'user_id':'666','user_psd':'666'}]
# 图书信息列表
library = [{'book_num':'111','book_name':'后街女孩','book_ads':'A111'},
           {'book_num':'222','book_name':'昧三皿','book_ads':'B222'},
           {'book_num':'333','book_name':'辉夜大小姐想让我告白','book_ads':'C333'},
           {'book_num':'444','book_name':'男子高中生的日常','book_ads':'D444'},
           {'book_num':'555','book_name':'在下坂本，有何贵干','book_ads':'E555'},]
# 账号检索模块
def check_user(user_id,user_psd):
    for userkey in user_info:
        if user_id in userkey['user_id']:
            if user_psd == userkey['user_psd']:
                print("登陆成功！")
                return 1
            else:
                print("密码不正确!")
                return 0
    else:
        print("账号不存在！")
        return 0

# 注册账号唯一检索模块
def check_userid(user_id):
    for userkey in user_info:
        if user_id in userkey['user_id']:
            print("已存在账号！")
            break
    else:
        print("账号不存在！")
        return 0

# 登陆模块
def login():
    while True:
        user_id = str(input("请输入用户账号："))
        user_psd = str(input("请输入用户密码："))
        if check_user(user_id,user_psd) == 1:
            break
        else:
            pass


# 注册模块
def logon():
    while True:
        user_id = str(input("请输入用户账号："))
        for userkey1 in user_info:    # 检测是否已存在用户账号
            if user_id in userkey1['user_id']:
                print("已存在账号！")
                break
        else:
            user_psd = str(input("请输入用户密码："))
            user_info.append({'user_id':user_id,'user_psd':user_psd})  # 将账号信息加入到用户信息列表中
            print("注册成功！")
            break


# 首页显示模块
def print_menu():
    print("=================欢迎进入图书管理系统=====================")
    print("【1】添加图书")
    print("【2】查询图书")
    print("【3】删除图书")
    print("【4】修改图书")
    print("【5】显示所有图书")
    print("【6】退出")


# 添加图书模块
def add_book():
    pass

# 查询图书模块
def find_book():
    pass

# 删除图书模块
def delete_book():
    pass

# 修改图书模块
def revise_book():
    pass

# 显示所有图书模块
def show_books():
    print("以下为全部图书信息：")
    for book_mse in library:
        print("图书编号{0}，图书名《{1}》，图书位置{2}".format(book_mse['book_num'],book_mse['book_name'],book_mse['book_ads']))
    while True:
        order = int(input("返回上首页，请输入【1】"))
        if order == 1:
            break
        else:
            print("无法识别指令！")

# 主程序
def main():
    while True:
        in_or_on = int(input("欢迎使用图书管理系统，账号登陆请输入【1】，用户注册请输入【2】，退出请输入【0】"))
        if in_or_on == 1:
            login()    # 登陆
            break
        elif in_or_on == 2:
            logon()    # 注册
        elif in_or_on == 0:
            print("感谢您的使用！再见！")
            quit()     # 退出
        else:
            print("无法识别指令！")
    while True:
        print_menu()
        order = int(input("请根据上述提示，输入操作编号："))
        if order == 1:  # 添加图书
            add_book()
        elif order == 2:  # 查询图书
            find_book()
        elif order == 3:  # 删除图书
            delete_book()
        elif order == 4:  # 修改图书
            revise_book()
        elif order == 5:  # 显示所有图书
            show_books()
        elif order == 6:  # 退出
            print("感谢您的使用，再见！")
            break
        else:
            print("无法识别指令")

main()