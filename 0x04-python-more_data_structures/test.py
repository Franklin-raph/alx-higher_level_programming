# def only_diff_elements(set_1, set_2):
#     new_list = []
#     for i in set_2:
#         for j in set_1:
#             k = i + j
#             new_list.append(k)
#     return new_list

# set_1 = { "Python", "C", "Javascript" }
# set_2 = { "Bash", "C", "Ruby", "Perl" }
# print(only_diff_elements(set_1, set_2))


# def only_diff_elements(set_1, set_2):
#     new_list = []
#     for i in set_2:
#         for j in set_1:
#             if i == j:
#                 pass
#             else:
#                 k = i + j
#                 new_list.append(k)
#     return new_list

# set_1 = { "Python", "C", "Javascript" }
# set_2 = { "Bash", "C", "Ruby", "Perl" }
# print(only_diff_elements(set_1, set_2))


def multiply_by_2(a_dictionary):
    new_dict = {}
    dictionary_values = a_dictionary.copy()
    for i in dictionary_values:
        new_dict[i] = dictionary_values[i] * 2
        ans = dict(sorted(new_dict.items()))
        for key, val in ans.items():
            return key

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print(a_dictionary)
print("--")
print(new_dict)
