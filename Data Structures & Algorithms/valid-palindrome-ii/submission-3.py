class Solution:
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True

        n = len(s)
        left = 0
        right = n-1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s[left + 1 : right + 1]) or self.isPalindrome(s[left:right])
            left += 1
            right -= 1
        
    def isPalindrome(self,s):
        return s == s[::-1]