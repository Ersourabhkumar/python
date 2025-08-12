# '''abstractmethod'''
# from abc import abstractclassmethod , ABC
# class shape(ABC):
#     @abstractclassmethod
#     def area(self):
#         pass
# class triangle(shape):
#     def area(self,a,b):
#         self.a=a
#         self.b=b
#         print(0.5*self.a*self.b)
#     def m1(self):
#         print("i am m1")
# # class rectange(shape):
# #     def area(self,a,b):
# #         self.a=a
# #         self.b=b
# #         print(self.a*self.b)
# # obj=rectange()
# # obj.area(90,10)
# obj=triangle()
# obj.area(2,5)
# obj.m1()

"""starticmethod"""
# class c1:
#     data=90
#     # def m1(self,a):
#     #     self.a=a
#     @staticmethod
#     def m1():
#         a=10
#         b=90
#         c1.data=89
#         print(c1.data)
#         print("im m1 from startic")
#         # print(self.a)
# obj=c1()
# obj.m1()

"""classmethod"""
'''class method is a method which is bound '''
class c1:
    data=90

    @classmethod
    def m1(cls):
        cls.a=100
        cls.data=89
obj=c1()
obj.m1()
print(c1.data)
print(c1.a)
