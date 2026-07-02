class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum, maxsum = 0, float("-inf")
        for i in range(len(nums)):
            cursum += nums[i]

            if cursum > maxsum:
                maxsum = cursum
            
            if cursum < 0:
                cursum = 0
        return maxsum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna