class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        i = 0
        l = len(pat)
        while i < len(txt):
            if txt[i:l] == pat:
                return i
            i += 1
            l += 1
        return -1
                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna