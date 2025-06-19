# class Solution():
#     def selectionSort(self, nums):
#         for i in range(0, len(nums)):
#             self.min_index = i 
#             for j in range(i+1, len(nums)):
#                 if nums[self.min_index] >= nums[j]:
#                     self.temp = nums[j]
#                     nums[j] = nums[self.min_index]
#                     nums[self.min_index] = self.temp

                
#         return nums




# obj = Solution()
# arr = [1,79,90,4,56,7,34,3,53,57,4]
# result = obj.selectionSort(arr)

# for i in result:
#     print(i)



# class Solution():
#     def bubbleSort(self,arr):

#         for i in range(0, len(arr)):
#             for j in range(0, len(arr) - 1 - i):
#                 if arr[j] > arr[j+1]:
#                     temp = arr[j]
#                     arr[j] = arr[j+1]
#                     arr[j+1] = temp

#         return arr



# obj = Solution()
# arr = [1,79,90,4,56,7,34,3,53,57,4,5]
# result_arr = obj.bubbleSort(arr)
# for i in result_arr:
#     print(i)




# class Solution():
#     def insertionSort(self,arr):
#         for i in range(0, len(arr)): # 0 to 8
#                 j = i
#                 while j > 0 and arr[j-1] > arr[j]:
#                     temp = arr[j]
#                     arr[j] = arr[j-1]
#                     arr[j-1] = temp
#                     j = j-1
#         return arr




# obj = Solution()
# arr = [1,3,56,89,23,2,4,68,62] 
# result = obj.insertionSort(arr)
# for i in result:
#     print(i)





class Solution():
    def mergeSort(self,arr,low,high):
        if low >= high: 
            return
        else:
            mid = (low+high) // 2
            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid+1, high)
            sorted_array = self. merge_array(arr, low,mid, mid+1, high)
            return sorted_array


    def merge_array(self,arr, low, mid1, mid2, high):
        result = []
        
        left_pointer = low
        right_pointer = mid2

        while left_pointer <= mid1 and right_pointer <= high:

            if arr[left_pointer] <= arr[right_pointer]:
                result.append(arr[left_pointer])
                left_pointer += 1
            else:
                result.append(arr[right_pointer])
                right_pointer += 1
        

        while left_pointer <= mid1:
            result.append(arr[left_pointer])
            left_pointer += 1
        while right_pointer <= high:
            result.append(arr[right_pointer])
            right_pointer += 1
        
        for i in range(low, high+1):
            arr[i] = result[i-low]
        
        return arr

obj = Solution()
arr = [2,4,3,34,67,55,5,7,8,88,76,65,58] ## 12
low = 0
high = len(arr) - 1
result = obj.mergeSort(arr,low,high)

for i in result:
    print(i)