'''exception handling'''
# num1=int(input("Enter the first number :"))
# num2=int(input("Enter the second number :"))
# print(num1/num2)

#Exception => is the way to control the error during the execution
# Division by zero
# File not found
# Null or None reference access
# Network timeouts

try:
    num1=int(input("Enter the first number :"))
    num2=int(input("Enter the second number :"))
    print(num1/num2)
except Exception as e:
    print(e)