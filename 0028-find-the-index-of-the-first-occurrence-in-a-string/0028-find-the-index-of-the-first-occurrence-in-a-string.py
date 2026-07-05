class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        l = len(needle)
        while i < len(haystack):
            if haystack[i:l] == needle:
                return i
            i += 1
            l += 1
        return -1

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna