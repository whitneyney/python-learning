# 有红、黄、蓝三种颜色的球，其中红球 3 个，黄球 3 个，绿球 6 个。
# 先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。

for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(0, 7):
            if red + yellow + green == 8:
                print(f"红球有{red}个，黄球有{yellow}个，绿球有{green}个")

