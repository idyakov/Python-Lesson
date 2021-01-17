string = input()
string = string.replace(" ","").lower()
if string == string[::-1]:
    print("Yes")
else:
    print("No")