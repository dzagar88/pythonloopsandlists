mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below:
def types_of_values(list):
    for value in list:
        print(type(value))
types_of_values(mix)
