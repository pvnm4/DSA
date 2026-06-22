# Better Approach
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
       nums.sort()
       n = len(nums)
       ans = []

       for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
             continue
            j = i+1
            k = n-1
            while j < k:
                cursum = nums[i] + nums[j] + nums[k]
                if cursum < 0:
                    j += 1
                elif cursum > 0:
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

       return ans
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna