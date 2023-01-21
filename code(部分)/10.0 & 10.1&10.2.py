# 假设给定以下列表：
# member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
# 要求将列表修改为：
# member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

# 方法一：使用 insert() 和 append() 方法修改列表。
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
member.insert(1, 88)
member.insert(3, 90)
member.insert(5, 85)
member.insert(7, 90)
member.append(88)
print(member)

# 方法二：重新创建一个同名字的列表覆盖。
member1 = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
member1 = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
print(member1)

# 10.1 利用 for 循环打印上边 member 列表中的每个内容
for x in member:
    print(x)

# 10.2 修改一下代码打印的样式
# 方法1：
index = 0
while index < 10:
    print(member[index],member[index+1])
    index += 2

# 方法2：
for index in range(0, 10, 2):
    print(member[index], member[index+1])

