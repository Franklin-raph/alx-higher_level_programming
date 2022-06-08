def only_diff_elements(set_1, set_2):
    new_list = []
    for i in set_2:
        for j in set_1:
            k = i + j
            new_list.append(k)
    return new_list

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
print(only_diff_elements(set_1, set_2))


def only_diff_elements(set_1, set_2):
    new_list = []
    for i in set_2:
        for j in set_1:
            if i == j:
                pass
            else:
                k = i + j
                new_list.append(k)
    return new_list

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
print(only_diff_elements(set_1, set_2))