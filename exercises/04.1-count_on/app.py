my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

new_list = []

for value in my_list:
    if type(value) == type(dict()) or type(value) == type(list()):
        new_list.append(value)

print(new_list)
