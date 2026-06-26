class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        maxArea = 0

        while left < right:
            if height[left] > height[right]:
                minHeight = height[right]
            else:
                minHeight = height[left]
            # minHeight = min(height[left],height[right])
            
            width = right - left
            area = minHeight * width

            if area > maxArea:
                maxArea = area

            # maxArea = max(maxArea, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna