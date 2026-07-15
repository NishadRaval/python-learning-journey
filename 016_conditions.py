# a = 20

# if a > 18:
#     print("adult")

# elif a == 0:
#     print("invalid age")

# else:
#     print("not adult")

dict1 = {
    "nishad" : "python1234",
    "rahi" : "abc123",
}

name = input("Enter your name: ").lower()
password = input("Enter your password: ")

if name in dict1:
    if password == dict1[name]:
        print("login successful")
    else:
        print("invalid password")
else:
    print("invalid username")   