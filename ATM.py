"""create a ATM program through Exception handling """
print("welcome to atm")
amount=1000
A=input("press the key(withdrawal,deposite,check balance)")
if A=="withdrawal":
    E=int(input("Enter amount: "))
    try:
        if E<=amount:
            amount=amount-E
            print("secussfully withdrawal renmaining amount=",amount)
        else :
            raise Exception ("Enter valid amount")
    except Exception as e:
        print(e)
elif A=="deposite":
    D=int(input("Enter deposite amount: " ))
    try:
        if D<=0:
            raise Exception ("plz Enter valid input")
        else:
            amount=D+amount
            print("your new balance is : ",amount)
    except Exception as e:
        print(e)
elif A=="check balance":
    print(amount)
else:
    print("plz press valid key")