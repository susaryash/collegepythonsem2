# Set example (version 3)

x = {1, 3, 5, 7}
y = {5, 7, 9, 11}

print("Set X:", x)
print("Set Y:", y)

# Membership
print("Is 3 in X?", 3 in x)

# Looping
print("Iterating X:")
for e in x:
    print(e)

# Operations
print("Union:", x | y)
print("Intersection:", x & y)
print("Only in X:", x - y)
print("Only in Y:", y - x)
