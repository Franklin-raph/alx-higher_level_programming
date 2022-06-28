s1 = [1,2,3]
s2 = s1
# print(s1 is s2)

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

def increment(n):
    n.append(4)

l = [1, 2, 3]
print(l)
increment(l)