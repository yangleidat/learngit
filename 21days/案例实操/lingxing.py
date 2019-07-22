'''
控制台打印菱形

'''

N = 8
for i in range(N):
    #判断第一行
    if i == 0:
        print(' ' * (N - 1) +'*')
    else:
        s = ' ' * (N - (i + 1)) + '*' + (i * 2 - 1) * ' ' + '*'
        print(s)

for j in range(N-2,-1,-1):
    if j == 0:
        print(' ' * (N - 1) +'*')
    else:
        s1 = ' ' * (N - (j + 1)) + '*' + (j * 2 - 1) * ' ' + '*'
        print(s1)