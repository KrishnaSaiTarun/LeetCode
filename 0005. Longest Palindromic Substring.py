class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        start = 0
        end = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and (i+1 == j or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if end-start+1 < j-i+1:
                        start=i
                        end=j
        return s[start:end+1]
