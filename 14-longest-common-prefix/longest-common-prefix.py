class Solution(object):
    def longestCommonPrefix(self, strs):
        import os

        
        prefix = os.path.commonprefix(strs)
        return prefix
