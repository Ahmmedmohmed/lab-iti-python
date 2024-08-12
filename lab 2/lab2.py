import math

# Function to calculate the area 
def c_area(sh, r1, r2=0):
    if sh == "t":  # Triangle
        ar = 0.5 * r1 * r2
        return ar
    elif sh == "r":  # Rectangle
        ar = r1 * r2
        return ar
    elif sh == "s":  # Square
        ar = r1 * r1
        return ar
    elif sh == "c":  # Circle
        ar = math.pi * (r1 ** 2)
        return ar
    else:
        return "Invalid shape name"  

print(c_area("c", 4))     
print(c_area("t", 4, 3)) 
print(c_area("s", 4))    

# Function to find the indices of a specific character in a string
def find_char_indices(string, char):
    indices = []
    for index, c in enumerate(string):
        if c == char:
            indices.append(index)
    return indices

print(find_char_indices("ahmed", "a")) 

# Function to generate a multiplication table up to a given number
def table_m(number):
    table = []
    for i in range(1, number + 1):
        r = []
        for j in range(1, i + 1):
            r.append(i * j)
        table.append(r)
    return table

print(table_m(3))  

# Function to convert a list of elements into a dictionary with the first letter as key
def convert_to_dict(lst):
    d = {}
    for item in lst:
        d[item[0]] = item
    return d

print(convert_to_dict(["ahmed", "mohmed", "ahmed"]))  



 
