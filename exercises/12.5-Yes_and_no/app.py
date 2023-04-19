theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def map_bools(number):
    if number == 1:
        text = "wiki"
    else:
        text = "woko"
    return text
new_list = list(map(map_bools, theBools))
print(new_list)
    
