class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        for i in s:
            if i.isalnum():
                cleaned += i
        cleaned = cleaned.lower()
        left = 0
        right = len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True