class Solution:
    def leaders(self, arr):
        # code here
        lea_so_far = arr[-1]
        leader = [arr[-1]]
        
        for i in range(len(arr)-2,-1,-1):
            if arr[i] >= lea_so_far:
                lea_so_far = arr[i]
                leader.append(arr[i])
                
        leader.reverse()
        
        return leader
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna