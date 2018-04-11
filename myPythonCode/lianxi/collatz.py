'''
2018年4月9日
《Python编程快速上手》3.11项目实践之collatz序列
'''

def collatz(num):
	if num == 1:
		return num
	if num % 2 == 0:
		num = num // 2
		return num
	elif num % 2 ==1:
		num = 3 * num + 1
		return num

a = int(input("输入一个大于1的正整数：\n"))

while a > 1:
	a = collatz(a)
	print(a)