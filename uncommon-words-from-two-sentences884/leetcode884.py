class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        words = {}
        for i in s1.split(' '):
            if i in words:
                words[i] += 1
            else:
                words[i] = 1
        for i in s2.split(' '):
            if i in words:
                words[i] += 1
            else:
                words[i] = 1
        uncommon = []
        for i in words:
            if words[i]==1:
                uncommon.append(i)
        return uncommon

s1 = "apple apple"
s2 = "banana"

obj = Solution()
print(obj.uncommonFromSentences(s1, s2))