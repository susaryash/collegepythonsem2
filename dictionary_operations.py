# Dictionary program (version 3)

info = dict(name="Karan", age=21, course="CS")
print("Data:", info)

# Access safely
print("Course:", info.get("course"))

# Add & update
info.update({"age": 22, "city": "Pune"})
print("Modified:", info)

# Remove key
key = "name"
if key in info:
    del info[key]

print("Final dictionary:", info)
