class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        alpha = [0] * 26
        for letter in s:
            alpha[ord(letter) - ord('a')] += 1
        for letter in t:
            alpha[ord(letter) - ord('a')] -= 1
            if alpha[ord(letter) - ord('a')] < 0:
                return False 
        return True
