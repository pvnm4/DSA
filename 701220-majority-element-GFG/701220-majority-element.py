class Solution:
    def majorityElement(self, arr):
        #code here
        candidate = None
        count = 0
        for num in arr:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        freq = 0
        for num in arr:
            if num == candidate:
                freq += 1
                    
        if freq > len(arr) // 2:
            return candidate
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna