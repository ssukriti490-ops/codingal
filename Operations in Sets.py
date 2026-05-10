my_set = {1,2,3,4,4,4}
print("Set :" ,my_set)

my_set.add(5)
print("Updated Set:", my_set)

set1 = my_set
set2 = {2,4,4,6}

print("\nset 1", set1)
print("Set 2", set2)
print("Difference")
print(set1.difference(set2))
print("Symmeteric Difference")
print(set1.symmeteric_difference(set2))
setc1 = {"green","blue"}
setc2 = {"blue","yellow"}
print("Original sets:")
print(setc1)
print(setc2)
setc = setc1.union(setc2)
print("\nUnion of above sets:")
print(setc)