class Solution:
    def lexicalOrder(self, n):
        lex = 1
        # level = 1
        lexical = []
        for i in range(n):
            if lex<= n:
                lexical.append(lex)
                if lex*10 <= n:
                    lex *= 10
                    # level+=1
                while (lex+1)//10 > lex//10: 
                    lex = lex//10
                    # level-=1
                lex+=1

            else:
                while (lex+1)//10 > lex//10: 
                    lex = lex//10
                lex +=1
        return lexical