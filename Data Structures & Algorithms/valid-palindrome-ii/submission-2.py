class Solution:
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s[left+1 : right+1]) or self.isPalindrome(s[left : right])

            left += 1
            right -= 1

        return False

    def isPalindrome(self,s):
        return s == s[::-1]