# 生成一些可怕的诗歌，主要运用了random.int() 和random.choice()
import random

articles = ['a', 'the']  # 冠词
nouns = ['dog', 'man', 'woman', 'cat', 'donkey', 'bird']  # 名词
verbs = ['sang', 'ran', 'jumped','laughed']  # 动词
adverbial = ['loudly', 'quietly', 'well', 'badly']  # 状语
str = input("请输入希望生成的诗歌行数：")
try:
    rows = int(str)
    row = 0
    while row < rows:
        sentencestype = random.randint(1, 2)        # 选择句子结构
        if (sentencestype == 1):
            print(random.choice(articles) + " " + random.choice(nouns) + " " + random.choice(verbs))  # 冠词+名词+动词
        else:
            print(          # 冠词+名词+动词+状语
                random.choice(articles) + " " + random.choice(nouns) + " " + random.choice(verbs) + " " + random.choice(
                    adverbial))
        row+=1
except ValueError as err:
    print(err)
