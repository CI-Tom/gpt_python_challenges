num_list1 = [2, 42, 57, 3, 39, 71, 83]
even_only = []

for i in num_list1:
    if i % 2 == 0:
        even_only.append(i)

print(even_only)

# Alternative
num_list2 = [2, 42, 57, 3, 39, 71, 83]

new_list = [x for x in num_list2 if x % 2 == 0]

print(new_list)
