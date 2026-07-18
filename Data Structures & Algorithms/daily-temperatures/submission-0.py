class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        n  = len(t)
        ans =[0]*n
        stk =[]
        for i,a in enumerate(t):
            while stk and stk[-1][0]<a:
                stk_a,stk_i =stk.pop()
                ans[stk_i] = i -stk_i
            stk.append((a,i))
        return ans
        