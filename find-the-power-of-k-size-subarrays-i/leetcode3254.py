class Solution:
    def resultsArray(self, nums, k) :
        def findBiggest(start, ptr, k):
            while ptr+1<start+k:
                if nums[ptr]+1 != nums[ptr+1]:
                    if ptr ==start:
                        ptr +=1
                    return -1, ptr
                else:
                    ptr +=1
            r = nums[ptr]
            if ptr==start:
                ptr+=1
            return r, ptr
        result = []
        start = 0
        ptr = 0
        n = len(nums)
        while start+k<n+1:
            r, ptr = findBiggest(start, ptr, k)
            result.append(r)
            start +=1
        return result
            