# message = input('等待您填写：')
# print(message)
#挂起

# age = input('how old are you')
# print(age)
#
# age=int(age)
#
# age += 1
# print('next year you will be?')
# print(age)

# prompt = '\ntell me something, and i will repeat it back up to you'
# prompt += "\nenter 'quit' to end the program."
# message = ''
# while message!='quit':         # '!=' means '不是'
#     message = input(prompt)
#
#     if message!='quit':
#         print(message)

# prompt = '\ntell me something, and i will repeat it back up to you'
# prompt += "\nenter 'quit' to end the program."
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
#标志sign

# prompt = '\nplease enter the name of a city you have visited'
# prompt += "\nenter 'quit' when you are finished."
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("i'd love to go to " + city.title() + "!")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 1:
#         continue
#     print(current_number)

# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(current_user.title())

#pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)
#
# while 'dog' in pets:
#     pets.remove('dog')
#
# print(pets)

# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     responses[name] = response
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
for name, response in responses.items():
    print(name + " would like to visit " + response.title() + ".")


