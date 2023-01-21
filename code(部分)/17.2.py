def swift(x):
    """
    把十进制数转化为二进制数
    :param x:一个十进制数
    :return:一个二进制数
    """
    string = ''
    while 1:
        y = x % 2
        x = x // 2

        z = str(y)
        string = z + string  # 把每次对2求余的结果都加到前面（因为最后的那个结果再第一个）
        if x == 0:
            break
    return int(string)


print(swift(256))