class Solution:
    def __init__(self):
        self.hash_map = {}
    def mostFrequentElement(self,nums):
        for i in range(0 , len(nums)):

            if nums[i] in self.hash_map:
                self.hash_map[nums[i]] += 1
            else:
                self.hash_map[nums[i]] = 1
        
        self.max_hash = self.hash_map[nums[0]]
        print(len(self.hash_map))
        print(self.hash_map)
        print(self.max_hash)
        for i in range(1, len(self.hash_map)):
            print(self.hash_map[nums[i]])
            if self.hash_map[nums[i]] > self.max_hash:
                self.max_hash = self.hash_map[nums[i]]
            elif self.hash_map[nums[i]] == self.max_hash:
                return min(self.hash_map[i], self.max_hash)
        
        return self.max_hash


obj = Solution()
nums = [1,2,2,3,3,3]
result = obj.mostFrequentElement(nums)
print(result)