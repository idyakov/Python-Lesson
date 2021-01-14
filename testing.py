a = int(input("Please insert you name?"))
if a == 10:
    print("The number you have insert equal 10")
    print("well done!")
if a < 10:
    print("The number you have insert below then 10")
    print("well done!")
if a > 10:
    print("The number you have insert over then 10")
    print("well done!")

a = int(input("Please inster yout number"))
if a > 5:
    print(a)

operator
ELSE

a = int(input("Please insert you name?"))
if a == 10:
    print("The number you have insert equal 10")
    print("well done!")
else:
    print("Unfortunately the number you have dial is not available ")

# Inser your password
password = 'password'
user_password = input('Please insert your password?')
if password == user_password:
    print("Входите")
else:
    print('Доступ запрещен')

# elif
a = int(input("Insert the number?"))
if a > 10:
    print("the number is over then 10")
elif a == 10:
    print("this is 10")
elif a == 0:
    print("equal 0")
else:
    print("this is not then 10")

# temperature
t = int(input("please insert the temperature outside"))
if t < -4:
    print("морозно")
elif t < 0 and t >= -4:
    print("холодно")
elif t >= 0 and t < 12:
    print("прохладно")
elif t >= 12 and t < 23:
    print("тепло")
elif t >= 27:
    print("жарко")

a = int(input("Please insert the numbers?"))
if a > 10 and a < 20:
    print('this number is over than 10 but below then 20 ')

a = int(input("Please insert the numbers?"))
if a > 10:
    if a < 20:
        print('this number is over than 10 but below then 20 ')

# UpperCase
print("hello, world!".upper())

# UpperCase with variables
string = input("Insert the line which you prefer").upper()
print(string)

# Calculator
a = input("Insert the number please?")
b = input("Insert the number please?")
if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    result = str(a + b)
    print(result)
else:
    print("this is not numbers")

# Count of numbers function len
string = input()
if len(string) > 5:
    print("Wrong! You insert over then 5 digits")
elif not string:
    print("Error! Insert something please")
else:
    print("you insert less then 5 digits")