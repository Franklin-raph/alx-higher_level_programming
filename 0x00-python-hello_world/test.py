from pip import main


def palindrome(str):
    inputVal = str[::-1]
    if(inputVal == str):
        print("palidrome")
    else:
        print("Not palindrome")

palindrome("nursesrun")

mainList = [0,2,1,4,3]
print(mainList)
mainList.pop(1)
print(mainList)

myfile = open('myfile.txt')
myfile = open("C:\\Users\Franklin Chinedu\Desktop\AccontPass.txt")

# reading from a file
print(myfile.read())
myfile.close()