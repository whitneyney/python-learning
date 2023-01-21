print('|---欢迎进入通讯录程序\t---|')
print('|---1：查询联系人资料\t---|')
print('|---2：插入新的联系人\t---|')
print('|---3：删除已有联系人\t---|')
print('|---4：退出通讯录程序\t---|')


mydict = {}
while 1:
    num = int(input('请输入相关的指令代码：'))
    if num ==4:
        break
    name = input('请输入联系人姓名：')
    if num == 2:
        if name not in mydict:
            mydict[name] = input('请输入用户联系电话：')
        else:
            print(f'您输入的姓名在通讯录中已存在-->>{name}：{mydict[name]}')
            option = input('是否修改用户资料(YES/NO):')
            if option == 'YES':
                mydict[name] = input('请输入用户联系电话：')
    elif num == 1:
        print(f'{name}：{mydict.get(name)}')
    else:
        mydict.pop(name)
