class Solution(object):
    def letterCombinations(self, digits):
        phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }

    # Base case
        if not digits:
            return [""]   # important: return list with empty string

        first = digits[0]
        rest = digits [1:]

        result = []

    # Recursive call
        rest_combinations = self.letterCombinations(rest)
    
        for ch in phone[first]:
            for r in rest_combinations:
                result.append(ch + r)

        return result

        