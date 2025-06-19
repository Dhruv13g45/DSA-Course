# class Solution():
#     def selectionSort(self, arr): ## comparing element with highest index
#         for i in range(0, len(arr)) : ## outer loop for passes or rounds no of times to iterate the loop
#             min_index = i
#             for j in range(i, len(arr)): ## checking min element with every element
#                 if arr[j] <= arr[min_index]:
#                     temp = arr[j]
#                     arr[j] = arr[min_index]
#                     arr[min_index] = temp
#         return arr

#     def bubbleSort(self, arr):
#         for i in range(len(arr)-1, 0, -1): ## outer loop for passes and rounds or no of times to iterate the loop
#             for j in range(0, len(arr) - i): ## pushing the max element at the end of the list
#                 if arr[j] >= arr[j+1]:
#                     temp = arr[j]
#                     arr[j] = arr[j+1]
#                     arr[j+1] = temp
#         return arr


#     def insertionSort(self,arr):
#         for i in range(0, len(arr)): ## outer loop for passes and rounds or no of times to iterate the loop
#             j=i
#             while j > 0 and arr[j-1] > arr[j]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#                 j -= 1

#         return arr
        



# obj = Solution()
# arr = [1,4,3,67,8,5,66,9,0,565,86,54,-1,69]
# result1 = obj.selectionSort(arr)
# result2 = obj.bubbleSort(arr)
# result3 = obj.insertionSort(arr)

# # for i in result1:
# #     print(i)
# # for i in result2:
# #     print(i)
# for i in result3:
#     print(i)




class Solution():


    def sort_array(self, arr):
        
        for i in range(0, len(arr)):
            
            for j in range(len(arr)-i-1, 0 , -1):


                if arr[j] >= arr[j-1]:
                    temp = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = temp

        return arr


obj = Solution()
arr = [9,7,3,2,8]
result = obj.sort_array(arr)

for i in result:
    print(str(i) + " ", end='')