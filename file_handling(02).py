num = int(input(" "))
n = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if( n== rev):
    print("Yes")
else:
    print("no")
