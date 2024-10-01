class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = {}
        for i in arr:
            r = i %k
            if (k-r)%k in remainder and remainder[(k-r)%k ]>0:
                remainder[(k-r)%k] -= 1
            else:
                if r in remainder:
                    remainder[r]+=1
                else:
                    remainder[r] = 1
        for key in remainder:
            if remainder[key] != 0:
                return False
        else:
            return True