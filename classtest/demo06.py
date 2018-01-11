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


class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫%s，我演讲的主题是：%s" % (self.name, self.topic))


# 多重继承
class sample(student, speaker):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, "haha", t)


test = sample("Tom", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法，可以把speaker和student换一下顺序试试效果
