'''decorator==>which modify the properties and behavior of a method or properties we use @decorator name'''


# def f1(a):
#     print('hello')
# @f1
# def f2():
#     print("hye")
''''''
def f1(a):
    print('hello')
    a()#argument pass of f1 to calling f2 in f1 
@f1
def f2():
    print("hye")