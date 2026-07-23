class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sef =set()
        l =0
        long = 0
        n =len(s)
        for r in range(n):
            while s[r] in sef:
                sef.remove(s[l])
                l += 1

            w =(r-l) +1
            long =max(long,w)
            sef.add(s[r])
        return long 

        