class Solution:
    def countConsistentStrings(self, allowed, words):
        consistent = 0
        for word in words:
            for w in word :
                if w not in allowed:
                    break
            else:
                consistent+=1
        return consistent

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
obj = Solution()
print(obj.countConsistentStrings(allowed, words))