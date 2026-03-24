# Banking system (version 3)
import time

class Bank:
    def __init__(self):
        self.user = input("Enter name: ")
        self.acc = input("Enter acc no: ")
        self.balance = 800

    def menu(self):
        while True:
            print("\n1.Show 2.Add 3.Take 4.Exit")
            c = input("Choice: ")

            if c == "1":
                print("Balance:", self.balance)

            elif c == "2":
                amt = int(input("Deposit: "))
                self.balance += amt
                self.print_slip("Deposit", amt)

            elif c == "3":
                amt = int(input("Withdraw: "))
                if amt <= self.balance:
                    self.balance -= amt
                    self.print_slip("Withdraw", amt)
                else:
                    print("Not enough money")

            elif c == "4":
                break

    def print_slip(self, t, amt):
        print("\n--- RECEIPT ---")
        print(self.user, "|", self.acc)
        print("Type:", t)
        print("Amount:", amt)
        print("Balance:", self.balance)
        print("Time:", time.strftime("%H:%M:%S"))
        print("---------------")

obj = Bank()
obj.menu()
