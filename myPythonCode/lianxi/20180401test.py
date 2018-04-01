# 序数
# nums = range(1,10)
# for num in nums:
#     if num == 1:
#         print(str(num)+'st')
#     elif num== 2:
#         print(str(num)+'nd')
#     elif num == 3:
#         print(str(num)+'rd')
#     else:
#         print(str(num)+'th')
# 字典
# 6-1人 and 6-7人
people = {
    'xifu':{
        'first_name':'zhao',
        'last_name':'yan',
        'age':'34',
        'city':"xi'an"},
    'yanglei':{
        'first_name':'yang',
        'last_name':'lei',
        'age':'34',
        'city':"xi'an"
    }}
for name, people_info in people.items():
    Fullname = people_info['first_name']+" "+people_info['last_name']
    print('\n'+name+"'s Fullname is "+Fullname.title()+'.')
    print(name+"'s age is "+people_info['age']+'.')
    print(name+"'s city is "+people_info['city'].title()+'.')
#6-2喜欢的数字
# ren_shu = {
#     '媳妇':10,
#     '我':7,
# }
# print(ren_shu)
#6-3词汇表
# cihuibiao = {
#     'if':'判断语句，如果条件为True则执行它下面的缩进的语句',
#     'while':'循环语句,如果他后面的表达式结果为True则执行它下面的缩进语句，知道表达式结果为False',
#     'in':'测试in左边的元素否包含在in右边的元素中',
# }
# for k, v in cihuibiao.items():
#     print(k+':\n  '+v)

