class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        res = []
        n = len(nums)
        def backtrack(i ,curr ,total):
            if total == target:
                res.append(curr[:])
                return
            if total>target or i == n:
                return
            #include
            curr.append(nums[i])
            backtrack(i+1,curr,total+nums[i])
            curr.pop()
            #skip
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1,curr,total)
        backtrack(0,[],0)
        return res