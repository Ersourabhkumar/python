"""list comprehension"""
# data=list(map(int,input().split(" ")))
# print(data)

"""data=[pattern for i in collection]"""
# data=[2*i for i in range(1,11)]
# print(data)

# data1=[1,2,3,4,5]
# data=[i**2 for i in data1]
# print(data)

# data1=[1,2,3,4,5]
# data=[f"*{i**2}*" for i in data1]
# print(data)

# data1=[1,2,3,4,5]
# data=[f"{"*"*(i**2)}{i**2}{"*"*(i**2)}" for i in data1]
# print(data)

"""convert 2nd list in to flatted"""
# data=[[1,2],[3,4],[5,6]]
# data2=[x for x in range(1,6) for x in range(1,3)]
# print(data2)

# data=[[1,2],[3,4],[5,6]]
# data2=[x for x in range(1,11) if x%2==0]
# print(data2)


# data=[[1,2],[3,4],[5,6]]
# flatted=[j for x in data for j in x]
# print(flatted)
"""convert a list of string into list of integer but include those element which are completely integer"""
# data=["abc",3,5,"addd"] #-->[3,5]
# filter=[x for x in data if type(x)==int]
# print(filter)