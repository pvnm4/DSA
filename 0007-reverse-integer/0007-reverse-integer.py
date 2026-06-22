class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        INTMAX = 2**31 - 1
        while x :
            ld = x%10
            x = x//10
            
            if result > INTMAX//10 or (result == INTMAX//10 and ld >7):
                return 0
            result = result*10 + ld
            
        return sign*result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna