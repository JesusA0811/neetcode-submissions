class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        maxWater = 0

        while left < right:
            base = right - left
            height = min(heights[left], heights[right])

            if base * height > maxWater:
                maxWater = base*height

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWater

        