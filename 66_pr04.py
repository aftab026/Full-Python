num = int(input("Enter the number: "))
Prime = True

for i in range(2, num):
    if(num%i == 0):
        Prime = False
        break
if Prime:
    print("This number is Prime")
else:
    print("This number is not Prime")
