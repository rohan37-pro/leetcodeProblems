#include <stdio.h>

int countConsistentStrings(char * allowed, char ** words, int wordsSize){
    int consistent = wordsSize;
    int diff = 0;
    int wina = 0;
    int w = 0, a=0;
    for (int word=0; word<wordsSize; word++){
        w = 0;
        diff = 0;
        while (words[word][w]){
            a=0;
            wina = 0;
            while (allowed[a]){
                if (words[word][w]==allowed[a]){
                    wina = 1;
                    break;
                }
                a++;
            }
            if (wina==0){
                consistent-=1;
                break;
            }
            w++;
        }
    }
    return consistent;
}

int main(){
    char * allowed = "ab";
    char * words[] = {"ad","bd","aaab","baa","badab"};
    int wordsSize = 5;
    printf("%d", countConsistentStrings(allowed, words, wordsSize));
    return 0;
}