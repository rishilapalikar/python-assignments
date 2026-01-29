#creating set
set1 = set()
print(set1)

#Accessing elements
set1 = set(["Geeks", "For", "Geeks."])
print("Geeks" in set1)

#Union of sets
A = {1, 2, 3}
B = {3, 4, 5}

# Union using | operator
union_set = A | B

print("Union of A and B:", union_set)

#Intersection of sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {5, 8, 9, 10}

intersection_set = set1.intersection(set2, set3)
print("Intersection using intersection():", intersection_set)

#Difference in sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Using the difference() method
difference_set = set1.difference(set2)
print("Difference using difference():", difference_set)
