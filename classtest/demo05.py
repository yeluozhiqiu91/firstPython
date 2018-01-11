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


# 单继承
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类构造
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说：我%d 岁了，在读%d年级" % (self.name, self.age, self.grade))


s = student("Tom", 10, 20, 5)
s.speak()
