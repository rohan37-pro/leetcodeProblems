class Solution:
    def xorQueries(self, arr, queries):
        xor = []
        for q in queries:
            x = arr[q[0]]
            for j in range(q[0]+1, q[1]+1):
                x = x ^ arr[j]
            xor.append(x)
        return xor