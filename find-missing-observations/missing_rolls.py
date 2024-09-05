class Solution:
    def missingRolls(self, rolls, mean, n) :
        rolls_sum = 0
        for i in rolls:
            rolls_sum += i
        m = len(rolls)
        missing_sum = (mean * (m+n)) - rolls_sum
        if missing_sum <= n*6 and missing_sum >= n*1:
            if missing_sum%n==0:
                return [missing_sum//n] * n
            else:
                arr = [missing_sum//n] * n
                arr.sort()
                remainder = missing_sum%n
                i = 0
                while remainder!=0:
                    a = 6-arr[i]
                    if remainder >= a:
                        arr[i] += a
                        remainder -=a
                    else:
                        arr[i] += remainder
                        remainder = 0
                    i+=1
                return  arr
        else:
            return []
        
# rolls = [4,2,2,5,4,5,4,5,3,3,6,1,2,4,2,1,6,5,4,2,3,4,2,3,3,5,4,1,4,4,5,3,6,1,5,2,3,3,6,1,6,4,1,3]
# mean = 2
# n = 53
# obj = Solution()
# print(obj.missingRolls(rolls, mean, n))
