class Solution:
    def maxWater(self, arr):
        # code here
        left = 0
        right = len(arr) - 1
        area = 0
        
        while left < right:
            
            area = max((right - left) * min(arr[left], arr[right]) , area)
            
            if arr[left] < arr[right] :
                left += 1
            else:
                right -= 1
                
        return area

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna