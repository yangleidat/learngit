shangpin = ([1,'iphone6s',5800],[2,'mac book',9000],[3,'coffee',32],[4,'python book',80],[5,'bicyle',1500])
shopingcart = []
salary = int(input('salary: '))
while True:
	for wupin in shangpin:
		print(wupin)

	xuangou = input('>>>:')
	if xuangou == 'quit':
		if shopingcart:
			print('您已购买以下物品：')
			for x in shopingcart:
				print(x)
			print('您的余额为：'+str(salary))
			print('欢迎下次光临')
			exit()
		else:
			print('您本次没有购物，期待您的下次光临')
			exit()
	else:
		for x in shangpin:
			if int(x[0]) == int(xuangou):
				if int(x[2]) > int(salary):
					print('您的余额不足')
					break
				else:
					shoping = []
					shoping.append(x[1])
					shoping.append(x[2])
					shopingcart.append(shoping)
					salary = salary - int(x[2])
					print("已加入"+str(x[1])+"到您的购物车，您的当前余额为："+str(salary))