class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0
        
        while l < r:
            # Площадь = ширина × меньшая высота
            water = (r - l) * min(height[l], height[r])
            max_water = max(max_water, water)
            
            # Двигаем низкую стенку
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_water