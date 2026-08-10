class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res ,sol = [] , []
        def backtrack(i):
            if i==n:
                res.append(sol[:])#this will copy sol
                return
            #no go this path    
            backtrack(i+1)
            #go this path
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res
        