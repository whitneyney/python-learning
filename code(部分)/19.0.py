print('----------RESTART------------')
op = input('请输入一句话')
list1 = list(op)
list2 = list1.copy()
list1.reverse()
if list1 == list2:
    print('是回文联')
else:
    print('不是回文联')