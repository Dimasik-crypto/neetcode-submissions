class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxl = 0
        data = set(nums)
        for num in nums:
            if num - 1 not in data:
                l = 1
                while num + l in data:
                    l += 1
                maxl = max(maxl, l)  
        return maxl