par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

# Create a dictionary to store the counts
counts = {}

def count(string):
    # Remove spaces and convert string to lowercase
    string = string.replace(" ", "").lower()    
    # Iterate over each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in counts:
            counts[char] += 1
        # Otherwise, add it to the dictionary with a count of 1
        else:
            counts[char] = 1
    # Return the dictionary of counts
    return counts

# Usage with the given string in the prompt:
counts = count(par)
print(counts)
