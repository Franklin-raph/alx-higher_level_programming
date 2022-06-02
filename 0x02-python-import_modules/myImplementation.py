# My own implementation

string = "79 10 -40 -300 89"
total = 0
print(string.split())
for i in string.split():
    nums = int(i)
    total += nums
print(total)