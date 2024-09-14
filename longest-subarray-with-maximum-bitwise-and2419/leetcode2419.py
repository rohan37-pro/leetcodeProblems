class Solution:
    def longestSubarray(self, nums) :
        maximum = 0
        samenum = 0
        ans = 1
        for i in nums:
            if i == maximum:
                samenum+=1
                if samenum>ans:
                    ans = samenum
            elif i > maximum:
                samenum = 1
                maximum = i
                ans = 1
            else:
                samenum = 0
        return ans
            