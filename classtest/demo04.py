class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        # 定义私有属性,私有属性在类外部无法直接进行访问
        self.__weight = w

    def speak(self):
        print("%s 说：我%d 岁了" % (self.name, self.age))


p = people("bob", 10, 20)
p.speak()
print(p.name)
