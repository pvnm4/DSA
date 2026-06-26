class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixsum = 0
        prefixmap = {0:1}

        for num in nums:
            prefixsum += num

            if (prefixsum-k) in prefixmap:
                count += prefixmap[prefixsum-k]

            prefixmap[prefixsum] = prefixmap.get(prefixsum,0) + 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna