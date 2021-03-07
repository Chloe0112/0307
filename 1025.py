# #bicycles = ['Giant','BMW','goodBoy','yamaha']
# #print(bicycles)
# #bicycles.remove('goodBoy')
# #print(bicycles)
#
# people = ['a','b','c']
# people.insert(0,'d')
# people.insert(2,'e')
# people.append('f')
# print(people)
#
# people = ['a','b,','c']
# people[1] = 'g'
# print(people)
#
people = ['d', 'a', 'e', 'b', 'c', 'f']
# del people[0]
# print(people)
# people.remove('a')
# print(people)
# people.pop(2)
# print(people)
#
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True) #排列
print(sorted(cars)) #临时排列
print(cars)
# cars.reverse() #倒序
# print(cars)
# 1 = len(cars) #len长度，列表中的个数
# print(len(cars))
# nums = [3,5,7,9]
# print(max(nums))
# print(min(nums))

# for value in range(1,11,2): #奇数
#     print(value)
#
# for value in range(2,11,2): #偶数
#     print(value)

# players = ['charles','martina','michael','florence','eli']
#
# print('Here are the first three playses on my team:')
# for player in players[:3]:
#     print(player.title())

# my_foods = ['pizza','carrot cake','kfc']
# friend_foods = my_foods[:] #复制列表
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print(my_foods)
# print("\nMy friends' favorite foods are:") #制表符 \n 换行符
# print(friend_foods)

#Tuple
dimensions = (200,30,50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200,30,22) #完全覆盖
for dimension in dimensions: #遍历元组
    print(dimension)
print(dimensions)





