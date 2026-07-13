class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        otv = []
        numbers = sorted(nums)
        n = len(numbers)
        
        for i in range(n - 2):
            
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            
            l, r = i + 1, n - 1
            while l < r:
                s = numbers[i] + numbers[l] + numbers[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    otv.append([numbers[i], numbers[l], numbers[r]])
                    l += 1
                    r -= 1
                   
                    while l < r and numbers[l] == numbers[l - 1]:
                        l += 1
                    
                    while l < r and numbers[r] == numbers[r + 1]:
                        r -= 1
        
        return otv