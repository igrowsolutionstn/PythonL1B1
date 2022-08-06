'''
Task: Bank operations
variables: name, balance, amount
Perform deposit and withdraw operations for a customer in a bank

Direction ---> don't change any of the existing code. please add your code only at placeholder #your code here
'''

def deposit(b,a):
    return b+a #your code here

def withdraw(b,a):
    return b-a #your code here

name = "Tom"
balance = 100
amount = 10
ch='w' #your code here

if ch=='w':
    balance = withdraw(balance, amount)
elif ch=='d':
    balance = deposit(balance, amount)
else:
    print('Invalid Choice')

print("Balance Money : ", balance) #your code here
