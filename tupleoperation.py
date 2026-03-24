# Tuple handling (version 3)

t = (100, 200, 300, 400)
print("Tuple:", t)

# Access
print("Second element:", t[1])
print("Last element:", t[-1])

# Slice
print("Subset:", t[1:3])

# Nested structure
mix = (("a", "b"), [1, 2], 9)
print("Nested:", mix)

print("Inner tuple:", mix[0][1])
print("Inner list:", mix[1][0])

# Multiply
print("Repeated:", ("Z",) * 5)
