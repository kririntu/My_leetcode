class Solution(object):
    def reverse(self,x):
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        if rev < 2**31-1:
            return sign * rev
        else:
            return 0