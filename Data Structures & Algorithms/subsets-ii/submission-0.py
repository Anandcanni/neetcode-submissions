class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        def backtrack(i , curr):
            if i == n:
                res.append(curr[:])
                return 
            #all subset that have i
            curr.append(nums[i])
            backtrack(i+1 , curr)
            curr.pop()
            #all subset without i
            while  i+1<n and  nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, curr)
        backtrack(0,[])
        return res

        