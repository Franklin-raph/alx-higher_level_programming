myList = [1,2,3,4,5,6,7,8,9,10]
for num in myList:
    if (num % 2 == 0):
        print(num)
    else:
        print("Odd number:{}".format(num))


num = 123
counter = 0
while(num != 0):
    if(num % 2 == 0):
        num = num / 2
        counter += 1
    elif(num % 2 != 0):
        num = num - 1
        counter += 1
print(counter)
