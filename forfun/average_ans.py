# 打印用户输入的数值、个数、和、最大值、最小值、平均值
num = input("enter a number or Enter to finish:")
numbers = []
while num:
    try:
        numbers.append(int(num))
        num = input("enter a number or Enter to finish:")
    except ValueError as err:
        print(err)
if len(numbers) > 0:
    max = 0
    min = 0
    averange = 0
    sum = 0
    count = len(numbers)
    print("您输入的值：", numbers)
    numbers.sort()                  # 调用sort()排序，从小到大排序
    min = numbers[0]
    max = numbers[len(numbers) - 1]
    i = 0
    while i < count:
        sum += numbers[i]
        i += 1
    averange = sum / len(numbers)
    print("输入的数字个数：", count)
    print("输入的数字和：", sum)
    print("最大值：", max)
    print("最小值：", min)
    print("平均值：", averange)
else:
    print("您没有输入任何数字哦！")
