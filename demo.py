# import datetime

# x = datetime.datetime.now()
# c_year = int(x.year)
# birth_year=input('what year you were born:')
# age= c_year-int(birth_year)
# print(f'your age is {age}')

# #assignmen 2
# user_name=input('Enter your username:')
# password=input('Enter your password:')
# encrypted_pass='*'* len(password)
# print(f'Hey {user_name} your password {encrypted_pass} is {len(password)} letter long.')

# basket=[1,2,3,4,5]

# print('a'>'A')

# # basket.append(100)
# # basket.extend([30])
# # print(basket)
# new_list=[1,2,3,45,'tom','dick']

# print(new_list)
# new_list=basket.pop(3)
# basket.remove(2)
# print(new_list)
# print(basket)
# print()

# x,y,z,*other=(1,2,3,4,5,6,7)

# my_tuple=(2,3,4)
# my_tuple.count(2)

# print(x,y,z,other)

# other[0]=9
# print(other)

#ternary operators

# is_friend=True

# can_message="message allowed" if is_friend else "message not allowed"
# print(can_message)

#conditional statements

my_list2=['a','b','c','d','d','e','f','f']
duplicate=[]
for item in my_list2:
  if my_list2.count(item)>1:
    if item not in duplicate:
      duplicate.append(item)

    #
print(duplicate)