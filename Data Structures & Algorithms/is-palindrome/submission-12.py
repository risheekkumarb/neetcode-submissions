class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [o for o in s if o.isalnum()]
        l,r = 0, len(s)-1
        while l<=r:
            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True