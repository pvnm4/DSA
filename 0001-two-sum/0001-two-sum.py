# Two Pass HashMap Method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i , num in enumerate(nums):
            indices[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in indices and indices[diff] != i:
                return [i,indices[diff]]

        return []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna