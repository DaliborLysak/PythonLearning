# init list
v = ["a", "b", "c"]
print(f"initial list: {v}")

# add element to list
v.append("d")
print(f"list after adding element: {v}")

# copy list
u = v.copy()
print(f"copied list: {u}")

# count element in list
print(f"count of c is {v.count("c")}")

# index of element in list
print(f"index of c is {v.index("c")}")

# insert element to list
v.insert(1, "x")
print(f"list after inserting element: {v}")

# pop element from list
v.pop(1)
print(f"list after popping element: {v}")

# remove element from list
v.remove("c")
print(f"list after removing element: {v}")

# reverse list
z = v.copy()
z.reverse()
print(f"reversed list: {z}")

# sort list
z.sort()
print(f"sorted list: {z}")

# clear list
v.clear()
print(f"cleared list: {v}")

# zip
animals = ["cat", "dog" ]
count = [5, 8, 13]
print()
print("zip:")
for animals, count in zip(animals, count):
    print(f"{animals}: {count}")

# enumerate
animals = ["cat", "dog" ]
print()
print("enumerate:")
for i, animals in enumerate(animals):
    print(f"{i}: {animals}")