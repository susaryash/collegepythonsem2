# List operations (version 3)

values = [2, 4, 6, 8, 10]
print("List elements:", values)

# Access
for i in range(len(values)):
    print(f"Index {i} -> {values[i]}")

# Modify
values += [12]
values.insert(0, 1)
print("Updated list:", values)

# Remove
del values[2]
print("After deletion:", values)

# Sorting
asc = sorted(values)
desc = sorted(values, reverse=True)
print("Ascending:", asc)
print("Descending:", desc)
