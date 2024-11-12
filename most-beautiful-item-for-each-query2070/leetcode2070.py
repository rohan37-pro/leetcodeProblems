class Solution:
    def maximumBeauty(self, items, queries):
        items.sort(key=lambda x: x[1], reverse=True)
        # n = len(items)
        beauties = []
        for i in queries:
            cuteness = 0
            for it in items:
                if it[0] <= i:
                    cuteness = it[1]
                    break
            beauties.append(cuteness)
        return beauties

        