class Solution:
    def prefixCount(self, words, pref) :
        co = 0
        for w in words:
            if w.startswith(pref):
                co+=1
        return co