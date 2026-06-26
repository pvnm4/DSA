class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = maxcount = 0
    
        for i in range(n):
            if nums[i] == 1:
                count += 1
                if count > maxcount:
                    maxcount = count
            else:
                count = 0

        return maxcount

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna