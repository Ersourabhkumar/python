"""instance variable"""
#whose value change from object to object
#declare==> self.vatiable_name
# class m1:
#     def c1(self,a,b):
#         self.a=a
#         self.b=b
#         return print(self.a*self.b)
# obj1=m1()
# obj1.c1(90,10)
# obj2=m1()
# obj2.c1(34,45)

'''instance variable with normal variable'''
# class m1:
#     data=100
#     def c1(self,a,b):
#         self.a=a
#         self.b=b
#         return print(self.a*self.b+m1.data)  #classname.vatiablename to access the variable
# obj1=m1()
# obj1.c1(90,10)

'''you can use your instace varibale  in any method of same class but method should  execute first '''
# class c1:
#     def m1(self,a,b):
#         self.a=a
#         self.b=b
#         return self.a+self.b
#     def m2(self):
#         print(self.a-self.b)
# obj1=c1()
# print(obj1.m1(30,40))
# obj1.m2()

"""modify instance"""

# class c1:
#     def m1(self,a,b):
#         self.a=a
#         self.b=b
#         return self.a+self.b
#     def m2(self):
#         print(self.a-self.b)
# obj1=c1()
# print(obj1.m1(30,40))
# obj1.a=1000 #modify
# print(obj1.a)

"""static variable"""
# class m1:
#     data=100 #static
#     def c1(self,a,b):
#         m1.new=9000 #static
#         self.a=a
#         self.b=b
#         return print(self.a*self.b)
# obj1=m1()
# obj1.c1(90,10)
# obj2=m1()
# obj2.c1(34,45)


''''''
# x=100
# def show():
#     global x
#     x=90
# show()
# print(x)

""""""
# class c1():
#     data=100
#     def m1(self):
#         c1.new=400

# obj=c1()
# obj.m1()
# print(c1.new)




