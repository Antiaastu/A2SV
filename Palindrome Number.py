class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        if x < 0:
            return False
        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10
        return rev == x
