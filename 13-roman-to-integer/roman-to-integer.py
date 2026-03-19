class Solution(object):
    def romanToInt(self, s):
        d = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        summ = 0
        n = len(s)
        for i in range(n-1):
            if d[s[i]] >= d[s[i+1]]:
                summ = summ + d[s[i]]
            else:
                summ = summ - d[s[i]]
        summ = summ + d[s[n-1]]
        return summ
            