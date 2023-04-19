
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filter_r_names(name):
    return name[0].lower() == "r"
resulting_names = list(filter(filter_r_names, all_names))
print(resulting_names)




