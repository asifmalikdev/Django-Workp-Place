# from collections import namedtuple
#
#
# class Solution():
#     def recursion(self, n):
#         print(n)
#         n-=1
#         if n>0:
#             return self.recursion(n)
#
#     def factoral(self, n):
#         return 1 if n==1 else n* self.factoral(n-1)
#
#     def nameprint(self, n):
#         if n==0:
#             return 0
#         else:
#             print("asif", n)
#             self.nameprint(n-1)
#     def oneton(self, n):
#         if n==0:
#             return 0
#         self.oneton(n-1)
#         print(n)
#     def mergesort(self, n):
#         if len(n)>1:
#             mid = len(n)//2
#             print(mid)
#             left = n[:mid]
#             right = n[mid:]
#             print(left, right)
#             self.mergesort(left)
#             self.mergesort(right)
#             i=j=k=0
#             while i<len(left) and j<len(right):
#                 if left[i]>right[j]:
#                     n[k]=right[j]
#                     j+=1
#                 else:
#                     n[k]=left[i]
#                     i+=1
#                 k+=1
#             if i<len(left):
#                 while i <len(left):
#                     n[k]=left[i]
#                     i+=1
#                     k+=1
#             if j<len(right):
#                 while j<len(right):
#                     n[k]=right[j]
#                     k+=1
#                     j+=1
#         return n
#
#     def Swaping(self, lis, i , j):
#         if i>= j:
#             return 0
#         temp = lis[j]
#         lis[j]=lis[i]
#         lis[i]=temp
#         i+=1
#         j-=1
#         self.Swaping(lis, i, j)
#
#
# obj = Solution()
# # obj.recursion(10)
# # print(obj.factoral(6))
# # obj.nameprint(5)
# # obj.oneton(5)
# # print(obj.mergesort([3,2,4,5,3,34,56,6,3,2,323,2,4,5,3,34,56,6,3,2,323,2,4,5,3,34,56,6,3,2,323,2,4,5,3,34,56,6,3,2,323,2,4,5,3,34,56,6,3,2,323]))
# # lis = [2,3,4,5,6,7]
# # obj.Swaping(lis, 0, len(lis)-1)
# # print(lis)
#
#
# def swaping(lis):
#     i,j=0,len(lis)-1
#     print("list 1",lis)
#     while i<j:
#         lis[i],lis[j]=lis[j],lis[i]
#         i+=1
#         j-=1
#     return lis
# lis1 = [1,2,3,4,3,2,1,2]
# lis2 = swaping(lis1)
# print("list 2:",lis2)
# if lis1==lis2:
#     print("it is palindrome")
# else:
#     print("not palindrome")
#
# # lis = [2,4,1]
# # swaping(lis)
# # print(lis)
# # x=3
# # y=4
# # lis.append()
# lis3 = [1,2,3,4,3,2,1,2]
# lis4 = [2,1,2,3,4,3,2,1]
# if lis3==lis4:
#     print("this one tooo")
from numpy.ma.extras import average


class Solution(object):
    # def isPalindrome(self, s):
    #     s2=[]
    #     s1=[]
    #     for char in s:
    #         if char.isalnum():
    #             c = char.lower()
    #             s1.append(c)
    #     return "".join(s1) == "".join(s1)[::-1]
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
            print(num, "hello", result)
            print("hello asif")
        return result


#
# obj = Solution()
# # print(obj.isPalindrome("r909r"))
# print(obj.singleNumber([4,1,2,1,2,4,5]))


class Circle:
    def __init__(self, radius):
        self._radius = radius
        print("in constructo", self._radius)

    @property
    def radius(self):
        print("inn radius getter", self._radius)
        return self._radius

    @radius.setter
    def radius(self, value):
        print("in setter", value)
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        print("area getter", self._radius)
        return 3.14159 * self._radius ** 2

# Usage
# circle = Circle(5)
# print(circle.radius)  # Accessing radius via getter
# print(circle.area) # Accessing area via getter
# circle.radius = 7 # Setting radius via setter
# print(circle.radius)  # Accessing radius via getter
#
# print(circle.area) # Accessing area via getter



class Student():
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks  = marks

    @property
    def total_marks_getter(self):
        return sum(self.marks)

    @property
    def average_getter(self):
        return average(self.marks)

    @property
    def grade_getter(self):
        avg = self.average_getter
        if avg>50:
            return "Pass"
        else:
            return "fails"

    def __str__(self):
        return (
            f"Name : {self.name}, Roll No: {self.roll_no}"
            f"Total : {self.total_marks_getter}\n"
            f"Avg : {self.average_getter}\n"
            f"Grade : {self.grade_getter}"
        )





student1 = Student("Axif Malik", "CS101", [85, 90, 78, 92, 88])
print(student1)
