'''exception handling'''
# num1=int(input("Enter the first number :"))
# num2=int(input("Enter the second number :"))
# print(num1/num2)

#Exception => is the way to control the error during the execution
# Division by zero
# File not found
# Null or None reference access
# Network timeouts

# try:
#     num1=int(input("Enter the first number :"))
#     num2=int(input("Enter the second number :"))
#     print(num1/num2)
# except Exception as e:
#     print(e)


# try:
#     num1=int(input("Enter the first number :"))
#     num2=int(input("Enter the second number :"))
#     print(num1/num2)
# except ZeroDivisionError:
#     num1=int(input("Enter the first number :"))
#     num2=int(input("Enter the second number :"))
#     print(num1/num2)

# except Exception as e:
#     print("teji")
# else:
#     print("no error occur")

# try:
#     num1=int(input("Enter the first number :"))
#     num2=int(input("Enter the second number :"))
#     print(num1/num2)
# except Exception as e:
#     print("teji")
# else:
#     print("no error occur")
# finally:
#     print("alwayes execute")


''' loop'''
# try:
#     num1=int(input("Enter the first number :"))
#     num2=int(input("Enter the second number :"))
#     print(num1/num2)
        
# except ZeroDivisionError:
#     while True:
#         try:
#             num1=int(input("Enter the first number :"))
#             num2=int(input("Enter the second number :"))
#             print(num1/num2)
#         except ZeroDivisionError:
#             True
        
#         else:
#             break

"""another method"""
# while True:
#         try:
#             num1=int(input("Enter the first number :"))
#             num2=int(input("Enter the second number :"))
#             print(num1/num2)
#         except ZeroDivisionError:
#             True
        
#         else:
#             break

# while True:
#         try:
#             num1=int(input("Enter the first number :"))
#             num2=int(input("Enter the second number :"))
#             print(num1/num2)
#             break
#         except ZeroDivisionError:
#             True
#         except ValueError:
#             True
"""use raise to  create exception """
# try:
#     age=int(input("Enter age: "))
#     if age<18:
#         raise Exception ("age error occured")  #intentionally generate (raise) an exception when we want to
#     else:
#         print("eligible for vote")
# except Exception as e:
#     print("error-->",e)

# """   """
# try:
#     age=int(input("Enter age: "))
#     if age<18:
#         raise Exception ("age error occured")  #intentionally generate (raise) an exception when we want to
#     elif age==18:
#         raise Exception ("age=18 ")
#     else:
#         print("eligible for vote")
# except Exception as e:
#     print("error-->",e)
# """ use this way to short  the code"""
# try:
#     age=int(input("Enter age: "))
#     if age<18:
#         raise Exception ("age error occured")  #intentionally generate (raise) an exception when we want to
#     print("eligible for vote")
# except Exception as e:
#     print("error-->",e)

"""create a ATM program through Exception handling """
# print("welcome to atm")
# amount=1000
# A=input("press the key(withdrawal,deposite,check balance)")
# if A=="withdrawal":
#     E=int(input("Enter amount: "))
#     try:
#         if E<=amount:
#             amount=amount-E
#             print("secussfully withdrawal renmaining amount=",amount)
#         else :
#             raise Exception ("Enter valid amount")
#     except Exception as e:
#         print(e)
# elif A=="deposite":
#     D=int(input("Enter deposite amount: " ))
#     try:
#         if D<=0:
#             raise Exception ("plz Enter valid input")
#         else:
#             amount=D+amount
#             print("your new balance is : ",amount)
#     except Exception as e:
#         print(e)
# elif A=="check balance":
#     print(amount)
# else:
#     print("plz press valid key")        
