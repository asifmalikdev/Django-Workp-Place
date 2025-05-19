from collections import namedtuple


class Solution():
    def recursion(self, n):
        print(n)
        n-=1
        if n>0:
            return self.recursion(n)

    def factoral(self, n):
        return 1 if n==1 else n* self.factoral(n-1)

    def nameprint(self, n):
        if n==0:
            return 0
        else:
            print("asif", n)
            self.nameprint(n-1)
    def oneton(self, n):
        if n==0:
            return 0
        self.oneton(n-1)
        print(n)
    def mergesort(self, n):
        if len(n)>1:
            mid = len(n)//2
            print(mid)
            left = n[:mid]
            right = n[mid:]
            print(left, right)
            self.mergesort(left)
            self.mergesort(right)
            i=j=k=0
            while i<len(left) and j<len(right):
                if left[i]>right[j]:
                    n[k]=right[j]
                    j+=1
                else:
                    n[k]=left[i]
                    i+=1
                k+=1
            if i<len(left):
                while i <len(left):
                    n[k]=left[i]
                    i+=1
                    k+=2
            if j<len(right):
                while j<len(right):
                    n[k]=right[j]
                    k+=1
                    j+=1
        return n



obj = Solution()
# obj.recursion(10)
# print(obj.factoral(6))
# obj.nameprint(5)
# obj.oneton(5)
print(obj.mergesort([3,2,4,5,3,34,56,6,3,2,323]))