class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        t =len(nums)
        l = 0
        r = t - 1
        while l<r:
            m = (l+r)//2
            if nums[m]>nums[r]:
                l = m +1
            else: 
                r = m
        return nums[l]
        
        
        