class Solution:
    def __init__(self):
        self.hash_map = {}
    def mostFrequentElement(self,nums):
        for i in range(0 , len(nums)):

            if nums[i] in self.hash_map:
                self.hash_map[nums[i]] += 1
            else:
                self.hash_map[nums[i]] = 1

        max_val = max(self.hash_map.values())
        max_keys = [k for k, v in self.hash_map.items() if v == max_val]
        return min(max_keys)

obj = Solution()
nums = [1,2,2,2,3,3,3]
result = obj.mostFrequentElement(nums)
print(result)