class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        left = mid = 0
        right = len(nums)-1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left +=1
                mid +=1

            elif nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -=1
                if nums[mid] == 1:
                    mid +=1
            else:
                mid += 1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna