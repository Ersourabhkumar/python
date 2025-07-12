# mylist=[10,20,30,40]
# x=mylist[0]
# for i in range(0,4):
#     if mylist[i]>x:
#         max=mylist[i]
# print(max)

'''find the even index position'''
# list=[10,2,3,4,5,6,78]
# sum=0
# for i in range(len(list)):
#     if i%2==0:
#         sum=sum+list[i]
#         print(list[i] )
# print("sum :",sum)

'''Q'''
# list=[10,2,3,4,5,6,78]
# sum=0
# for i in list:
#     sum=sum+i
# print("sum of all element :",sum)

# list=[10,2,3,4,5,6,78]
# sum=0
# newlist=[]
# for i in list:
#     sum=sum+i
#     newlist.append(sum)
# print("sum of all element :",sum)
# print("new list :",newlist)

'''Prime'''
# list=[10,2,3,4,5,6,78]
# for i in list:
#     for j in range(2,i+1):
#         if i%j==0:
#             print("not prime=",i)
#             break
#         else:
#             print("prime=",i)

'''
print 4 digit number
'''
# list=[5222,1234,12345,765,3456543,56654,6543]

# for i in list:
#     temp=i
#     count=0
#     while i>0:
#         i=i//10
#         count+=1
#     if(count==4):
#         print(count,temp)

'''palindrom in list'''
# l=[1,2,3,3,2,1]
# i=0
# j=len(l)
# count=0
# while i<=len(l)//2:
#     if(l[i]!=l[j-1]):
#         count=1
#         break
#     i+=1
#     j-=1
# if(count==0):
#     print("p")
# else:
    # print("np")


   


