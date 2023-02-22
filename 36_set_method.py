# creating an empty set

b = set()
print(type(b))

#adding value to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add((4,5,6))

print(b)

print(len(b)) #prints the length of this set

b.remove(5) #removes 5 from set b
print(b)

print(b.pop()) # remove an arbitrary element
print(b)

print(b.clear())
print(b)