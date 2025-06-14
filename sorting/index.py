class Solution():
    def selectionSort(self, nums):
        for i in range(0, len(nums)):
            self.min_index = i 
            for j in range(i+1, len(nums)):
                if nums[self.min_index] >= nums[j]:
                    self.temp = nums[j]
                    nums[j] = nums[self.min_index]
                    nums[self.min_index] = self.temp

                
        return nums




obj = Solution()
arr = [1,79,90,4,56,7,34,3,53,57,4]
result = obj.selectionSort(arr)

for i in result:
    print(i)