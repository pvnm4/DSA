class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1

        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum == target:
                return[left +1, right +1]
            elif curSum < target:
                left += 1
            else:
                right -= 1

        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna