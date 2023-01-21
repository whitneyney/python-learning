import random

print('----------猜拳游戏----------'.center(25))
print('剪刀：1  石头：2  布：3'.center(25))
print('游戏规则：三局两胜')


def play(user, compu):
    global point
    global game
    if (user == 1 and compu == 2) or (user == 2 and compu == 3) or (user == 3 and compu == 1):
        print(f'round {game}：这局电脑胜')
        point -= 1
    elif user == compu:
        print(f'round {game}：你和电脑出的一样，这局重来')
        game -= 1
    else:
        print(f'round {game}：这局你胜')
        point += 1


game = 1
point = 0
gesture = {1: '剪刀', 2: '石头', 3: '布'}
while game <= 3:
    print(f'----------round {game}----------'.center(30))
    player = int(input('请输入您要选择出的东西（输入1或2或3）'))
    computer = random.randint(1, 3)
    print(f'这局你出了：{gesture[player]}, 而电脑出了：{gesture[computer]}')
    play(player, computer)
    game += 1
    if point == 2:
        break

print('游戏结束')
if point >= 1:
    print('你赢了')
else:
    print('电脑赢了')

