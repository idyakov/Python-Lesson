a = input("Please insert you for number")
stars_count = len(a) - 4
stars = "*" * stars_count
if len(a) >= 8 and a.isdigit():
    print((stars) + (a[-4::]))
else:
    print("Error")

