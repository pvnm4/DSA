class Solution:
    def reverse(self, nums, p1, p2):
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,0,n-1)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna