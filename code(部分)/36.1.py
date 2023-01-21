class Rectangle:
    def __init__(self):
        self.length = 5
        self.width = 4

    def getrect(self):
        print(f'这个矩形的长是：{self.length}，宽是：{self.width}')

    def setrect(self):
        print('请输入矩形的长和宽')
        self.length = float(input("长："))
        self.width = float(input("宽："))

    def getarea(self):
        print(self.width * self.length)


rect = Rectangle()
rect.getrect()
rect.setrect()

rect.getrect()
rect.getarea()

