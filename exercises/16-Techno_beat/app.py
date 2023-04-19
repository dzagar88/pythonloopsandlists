def lyrics_generator(lst):
    result = ""
    ones_count = 0
    
    for i in lst:
        if i == 0:
            result += "Boom "
        elif i == 1:
            result += "Drop the base "
            ones_count += 1
            if ones_count == 3:
                result += "!!!Break the base!!! "
                ones_count = 0
                
    return result

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))