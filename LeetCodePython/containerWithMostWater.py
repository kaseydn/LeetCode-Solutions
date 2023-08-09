class Solution:
    def maxArea(self, height):
        _maxArea = 0
        #Two pointer solution
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            _maxArea = max(_maxArea, area)
            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
        return _maxArea
        