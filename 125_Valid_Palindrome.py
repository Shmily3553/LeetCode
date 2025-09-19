# This script is not accpected
# "0P" -> False, but I think it should return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        st = ''
        for char in s:
            if char.isalpha():
                st += char.lower()
        return st == st[::-1]