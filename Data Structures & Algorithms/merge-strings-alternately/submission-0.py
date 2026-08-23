class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        res = ""
        for i in range(min(m, n)):
            # if i < n:
            res+=word1[i]
            # if i < m:
            res+=word2[i]
        a=min(m,n)
        if word1:
            res+=word1[a:]
        if word2:
            res+=word2[a:]
        return res