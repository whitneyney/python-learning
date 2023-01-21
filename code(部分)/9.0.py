count = 3
key = 'FishC.com'
while count:
    kw = input("请输入密码")
    if key == kw:
        print("密码正确，进入程序")
        break
    elif '*' in kw:
        print(f'密码中不能含有*号，您还有{count}次机会！',end='')
        break
    else:
        print(f"密码错误！您还有{count-1}次机会！",end='')
        count -=1

