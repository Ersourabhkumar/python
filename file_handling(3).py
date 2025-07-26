"""file handling"""
# file=open("file-name.extension","mode")
'''
r-read
w-write
append-a
+->read and write
'''
# file=open("regex.txt","w")
# file.write("welcome too  regex")
# file.close()
# file=open("regex.txt","r")
# content=file.read()
# print(content)
# file.close()
# file=open("ragex.txt","a")
# file.write("append in the regex")
# file.close()

''''''
# file=open("regex2.txt","a")
# file.write("""i am inside regex2 file

# hyy

# this is a 

# hello""")
# file.close()
"""autoclose with """
# with open("regex.txt","r") as source,open("regex2.txt","a") as dastination:
#     for line in source:
#         destination.write("\n"+line)

# with open("regex.txt","r") as source, open("regex2.txt","r") as destination:
#     context1=source.read()
#     context2=destination.read()
#     print(context1)
#     print(context2)
# with open ("regex2.txt","r") as file:
#     count_char=0
#     count_str=0
#     for line in file:
#         ch=line.split()
#         count_str+=1
#         for i in line:
#             count_char+=1
# print(count_char,count_str)
        