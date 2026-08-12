class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='':
            return []
        res , sol = [],[]
        digit_pool={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        n = len(digits)
        def backtrack(i=0):
            if i == n :
                res.append(''.join(sol))
                return
            for digit in digit_pool[digits[i]]:
                sol.append(digit)
                backtrack(i+1)
                sol.pop()
        backtrack(0)
        return res

        