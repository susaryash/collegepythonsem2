# Library system (version 3)

books = ["DBMS", "AI", "ML"]

def show():
    print("Books available:", books)

def issue(b):
    if b in books:
        books.remove(b)
        print(b, "issued")
    else:
        print("Not available")

def submit(b):
    books.append(b)
    print(b, "returned")

show()
issue("AI")
show()
submit("AI")
show()
