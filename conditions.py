import sys

type = sys.argv[1]

if type == "t2.micro":
    print("We can create an instance and it chanrges 2$ a day")
elif type == "t4.micro":
    print("We can create an instance and it chanrges 8$ a day")
elif type == "t5.micro":
    print("We can create an instance and it chanrges 18$ a day")
else:
    print("We can cannot create an instance of the type", type)

