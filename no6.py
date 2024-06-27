def num_to_list(a):
    element_dict = {}
    for item in a:
        if item not in element_dict:
            element_dict[item] = []
        element_dict[item].append(item)
    return list(element_dict.values())
        

s=eval(input())
print(num_to_list(s))