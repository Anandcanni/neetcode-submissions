class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        if nums == []:
            return False
        for i in range(len(nums)):
            s.add(nums[i])
            if len(nums)==len(s):
                return False
        return True
                
        