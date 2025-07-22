print("welcome to flipkart")
print("1.cloths 2.shoes 3.jacket")
item=int(input("Enter the buyingg product"))
price=0
if item=="1":
    print("cloths")
    print("choose=> 1.1000 2.2000 3.3000")
    p=int(input("enter 1/2/3"))
    if p==1:
        print("choose Quantity")
        Q=int(input("1to 3"))
        if Q==1:
            print("your order is placed")
            price=1000
        elif Q==2:
            print("your order is placed")
            price=2000
        elif Q==3:
            print("your order is placed")
            price=3000
    elif p==2:
        print("choose Quantity")
        Q=int(input("1to 3"))
        if Q==1:
            print("your order is placed")
            price=2000
        elif Q==2:
            print("your order is placed")
            price=4000
        elif Q==3:
            print("your order is placed")
            price=6000
    elif p==3:
        print("choose Quantity")
        Q=int(input("1to 3"))
        if Q==1:
            print("your order is placed")
            price=3000
        elif Q==2:
            print("your order is placed")
            price=6000
        elif Q==3:
            print("your order is placed")
            price=9000
elif item=="2":
    print("shoes")
    print("shoes=> 1.500 2.1000 3.2000")
    p=int(input("enter 1/2/3"))
    if p==1:
        print("choose Quantity")
        Q=int(input("1to 3"))
        if Q==1:
            print("your order is placed")
            price=500
        elif Q==2:
            print("your order is placed")
            price=1000
        elif Q==3:
            print("your order is placed")
            price=1500
    elif p==2:
        print("choose Quantity")
        Q=int(input("1to 3"))
        if Q==1:
            print("your order is placed")
            price=1000
        elif Q==2:
            print("your order is placed")
            price=2000
        elif Q==3:
            print("your order is placed")
            price=3000
    elif p==3:
        print("choose Quantity")
        Q=int(input("1to 3"))
        if Q==1:
            print("your order is placed")
            price=1500
        elif Q==2:
            print("your order is placed")
            price=3000
        elif Q==3:
            print("your order is placed")
            price=4500
elif item=="3":
    print("jacket")
    print("jacket=> 1.1500 2.2000 3.4000")
    p=int(input("enter 1/2/3"))
    if p==1:
        print("choose Quantity")
        Q=int(input("1to 3"))
        if Q==1:
            print("your order is placed")
            price=1500
        elif Q==2:
            print("your order is placed")
            price=3000
        elif Q==3:
            print("your order is placed")
            price=4500
    elif p==2:
        print("choose Quantity")
        Q=int(input("1to 3"))
        if Q==1:
            print("your order is placed")
            price=2000
        elif Q==2:
            print("your order is placed")
            price=4000
        elif Q==3:
            print("your order is placed")
            price=6000
    elif p==3:
        print("choose Quantity")
        Q=int(input("1to 3"))
        if Q==1:
            print("your order is placed")
            price=4000
        elif Q==2:
            print("your order is placed")
            price8000
        elif Q==3:
            print("your order is placed")
            price=12000
print("your order is place in 3 days")