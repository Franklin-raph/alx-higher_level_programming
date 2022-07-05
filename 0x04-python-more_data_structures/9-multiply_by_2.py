
def multiply_by_2(a_dictionary):
    cpy = a_dictionary.copy()
    for i in cpy:
        cpy[i] = cpy[i] * 2
    return cpy

print(multiply_by_2({'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}))