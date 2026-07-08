class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1
        
        total_sum = sum(arr)
        
        expected_sum = n * (n+1) // 2
        
        return expected_sum - total_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna