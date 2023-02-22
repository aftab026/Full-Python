# write a program to find out whether a given post is talking about "Harry" or not.

post = "This  is talking about 'harry'"

name = input("Enter the name to check\n")


if name in post:
    print("yes")

else:
    print("no")