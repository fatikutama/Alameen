# def sing_happy_birthday():
#     print('happy birthday to you') 
#     print('happy birthday to you')
#     print('happy birthday to you')
#     print('happy birthday to you')

# sing_happy_birthday()

# def division (name, school):
#     return name +" "+ school
# print(division('fatima', 'ibrahim'))

# def passwordlength(password):

#     password = str(password)
#     length = len(password)

#     return length
# password = '12345678910'
# print (passwordlength(password))


# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

def my_function(*studentinfo):
    print("my name is" + studentinfo[0])
    print("i'm" + studentinfo[1])
    print("i am a student of" + studentinfo[2])
    print("faculty of" + studentinfo[3])
    print("department" + studentinfo[4])

my_function("fatima","23 yrs old","bayero universty","computing","computer science")