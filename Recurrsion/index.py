# class Solution():
#     def __init__(self):
#          self.fact = 1

#     def factorial(self,num):
              
#         if num == 0:
#                 return self.fact
#         else:
#                 self.fact *= num
#         return self.factorial(num-1)

# obj = Solution()
# num = 3
# result = obj.factorial(num)
# print(result)





# class Solution:
#     def __init__(self):
#         self.i=0
        
#     def reverse(self, arr, n):

#         if self.i >= n - 1:
#                 return arr
#         else:
#                 self.arr1_value = arr[self.i]
#                 arr[self.i] = arr[n-1]
#                 arr[n-1] = self.arr1_value
#                 self.i += 1
#                 n = n-1
#                 return self.reverse(arr, n)




# obj = Solution()
# n=5
# array = [1,2,3,4,5]
# result = obj.reverse(array,n)

# for i in result:
#     print(i)