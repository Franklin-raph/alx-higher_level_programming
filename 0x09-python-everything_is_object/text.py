s1 = [1,2,3]
s2 = s1
# print(s1 is s2)

# l1 = [1, 2, 3]
# l2 = l1
# l1 = l1 + [4]
# print(l2)

# def increment(n):
#     n.append(4)

# l = [1, 2, 3]
# print(l)
# increment(l)


def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

a = (1, 2)
b = (1, 2)
print("25 ans",a is b)





def copy_list(l): return l[:]

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)