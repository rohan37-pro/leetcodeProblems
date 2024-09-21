class Solution:
    def lexicalOrder(self, n):
        lex = 1
        i = 0
        lexical = []
        while i < n:
            if lex<= n:
                lexical.append(lex)
                i+=1
                if lex*10 <= n:
                    lex *= 10
                else:
                    lex+=1
                    while (lex)//10 > (lex-1)//10: 
                        lex = lex//10
            else:
                while (lex+1)//10 > lex//10: 
                    lex = lex//10
                lex +=1
        return lexical

# obj = Solution()
# print(obj.lexicalOrder(136))