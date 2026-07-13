from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for elem in nums:
            if elem not in s:
                s[elem] = 1  
            else:
                s[elem] += 1
        
        
        return sorted(s, key=s.get, reverse=True)[:k]