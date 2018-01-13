# 控制台输入数字串，输出用*号画出来的数字，将*号变成输入的数字
import sys

ZERO = ['  ***  ',
        ' *   * ',
        '*     *',
        '*     *',
        '*     *',
        ' *   * ',
        '  ***  '
        ]
ONE = [' * ',
       '** ',
       ' * ',
       ' * ',
       ' * ',
       ' * ',
       '***'
       ]
TWO = ['  *** ',
       ' *   *',
       '*   * ',
       '   *  ',
       '  *   ',
       ' *    ',
       '******'
       ]
ThREE = ['  **** ',
         ' *    *',
         '      *',
         '   ****',
         '      *',
         ' *    *',
         '  **** '
         ]
FOUR = ['    * ',
        '   ** ',
        '  * * ',
        ' *  * ',
        '******',
        '    * ',
        '    * '
        ]

FIVE = ['*****',
        '*    ',
        '*    ',
        '*****',
        '    *',
        '    *',
        '*****'
        ]

SIX = ['*****',
       '*    ',
       '*    ',
       '*****',
       '*   *',
       '*   *',
       '*****'
       ]
SEVEN = ['****',
         '   *',
         '   *',
         '   *',
         '   *',
         '   *',
         '   *'
         ]
EIGHT = ['****',
         '*  *',
         '*  *',
         '****',
         '*  *',
         '*  *',
         '****'
         ]
NIGHT = ['****',
         '*  *',
         '*  *',
         '****',
         '   *',
         '   *',
         '****'
         ]


# 打印单个数字
def printsingle(thenumber):
    for item in thenumber:
        print(item)


# 打印数字数组
def printall(allnumber):
    count = len(allnumber)
    row = 0
    while row < 7:
        start = 0
        line = ""
        while start < count:
            line += allnumber[start][row] + "  "
            start = start + 1
            if start == count:
                print(line)
        row = row + 1


digital = [ZERO, ONE, TWO, ThREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NIGHT]
# printall(digital)
# inputnumber=input("请输入一串数字：")
# dic=sys.argv[0]

try:
    inputnumber = input("请输入一串数字：")
    count = len(inputnumber)
    row = 0
    while row < 7:
        start = 0
        line = ""
        while start < count:
            temp = digital[int(inputnumber[start])][row] + "  "
            temp = temp.replace('*', inputnumber[start])                # 将*号替换成输入的数字
            line += temp
            start = start + 1
            if start == count:
                print(line)
        row = row + 1
except IndexError as error:
    print(error)
