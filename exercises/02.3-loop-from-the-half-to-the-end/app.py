my_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]

#Your code here:
initialValue = 7
stopValue = 14
increaseValue = 1

for i in range(initialValue, stopValue):
    if i == my_list[i]:
        i += increaseValue
    print(my_list[i])
