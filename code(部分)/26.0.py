def desk():
    print('|---新建用户：N/n\t---|')
    print('|---登录账号：E/e\t---|')
    print('|---退出程序：Q/q\t---|')


mydict = {}

while 1:
    desk()
    number = input('|---请输入指令代码：')
    if number == 'Q' or number == 'q':
        break
    while number != 'N' and number != 'n' \
            and number != 'E' and number != 'e':
        number = input('您输入的指令代码有误，请重新输入')
    name = input('请输入用户名：')
    if number == 'N' or number == 'n':
        while 1:
            if name in mydict:
                name = input('此用户名已经被使用，请重新输入：')
            else:
                break
        mydict[name] = input('请输入密码')
        print('注册成功，试试登录吧')
    else:
        while 1:
            if name not in mydict:
                name = input('您输入的用户名不存在，请重新输入：')
            else:
                break
        key = input('请输入密码：')
        while 1:
            if key == mydict[name]:
                print('欢迎进入系统')
                break
            else:
                key = input('您输入的密码有误，请重新输入密码')


