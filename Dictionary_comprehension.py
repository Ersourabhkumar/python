"""dictionary comprehension"""
# data1=(("a",10),("b",20))

# data={k:v for k,v in data1} #keys:values for keys,values in iterable
# print(data)

# data={x:x**2 for x in range(1,5)}
# print(data)

# data={'a': 10, 'b': 20}
# print(data.items())
# for k,v in data.items():
#     print(k,"--",v)

"""csv package"""
# import csv

# with open("data.csv","r") as file:
#     reader=csv.reader(file)
#     for i in reader:
#         print(i)

# import csv

# with open("data.csv","r") as file:
#     reader=csv.DictReader(file)
#     for i in reader:
#         print(i)

# import csv

# data=[["name","age"],["a",43],["b",32]]
# with open("datanew.csv","w") as file:
#     writer=csv.writer(file)
#     writer.writerows(data)
    
