# a = 35
# b = 94
# for x in range (1,a):
#     y = 35-x
#     if x*2+y*4==b:
#         print("鸡有"+str(x)+"只","兔有"+str(y)+"只")



# alien = {'color':'green','points':5} #key:value
#
# print(alien['color'])
# print(alien['points'])
#
# alien['x_position'] = 0
# alien['y_position'] = 25 #添加"键-值"

# alien_1 = {'color':'green'}
# print('The alien is '+alien_1['color']+'.')
#
# alien_1['color']='yellow'  #改
# print('The alien is now '+alien_1['color']+'.')

# alien_2 = {'x_position':0,'y_position':'25','speed':'medium'}
# print('Original x_position:'+ str(alien_2['x_position']))
# del alien_2['y_position']
# #向右移动外星人
# #根据外星人当前速度决定将其移动多元
#
# if alien_2['speed']=='slow':
#     x_increment = 1
# elif alien_2['speed']=='medium':
#     x_increment = 2
# else:
#     #这个外星人的速度一定是fast了
#     x_increment = 3
#
# alien_2['x_position']=alien_2['x_position']+x_increment
# print('New x_position:'+str(alien_2['x_position']))

# favourite_languages={
#     'Raven':'Python',
#     'Michael':'.net',
#     'Kevin':'swift',
# }
# print("Paven's favourite_language is " +
#       favourite_languages['Ravin'].title() +
#       '.')

# user_0 = {
#     'username':'Kevin',
#     'first':'zou',
#     'last':'Jiawen',
# }
# for key,value in user_0.items(): #key,value为两个临时变量
#     print('\nkey:' + key)
#     print('Value:' + value)

# favourite_languages={
#      'Raven':'python',
#      'Michael':'.net',
#      'Kevin':'swift',
# }
#
# # for name,language in favourite_languages.items():  #items用来取建值对
# #     print(name.title()+"'s favourite language is "+
# #           language.title()+'.')
#
# for name in favourite_languages.keys():  #keys用来取键
#     print(name.title())

# favourite_languages={
#       'Raven':'python',
#       'Michael':'.net',
#       'Kevin':'swift',
# }
#
# friends = ['Raven','Michael']
# for name in favourite_languages.keys():
#     print(name.title())
#
#     if name in friends:
#         print("Hi "+name.title()+
#               ", I see your favourite language is "
#               +favourite_languages[name].title()+"!")

# favourite_languages={
#        'Raven':'python',
#        'Michael':'.net',
#        'Kevin':'swift',
#  }
#
# print("The following languages have been mentioned:")
# for language in favourite_languages.values():  #values用来取所有的值
#    print(language.title())

#items  -> k-v
#keys   -> k
#values -> v

# alien_0 = {'color':'green','points':5}
# alien_1 = {'color':'yellow','points':10}
# alien_2 = {'color':'red','points':15}
#
# aliens = [alien_0,alien_1,alien_2]   #列表中嵌套字典
#
# for alien in aliens:
#     print(alien)


aliens = []

for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens:" + str(len(aliens)))


