class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())

        mid = len(s)//2
        first_part = s[:mid]
        second_part = s[mid:]

        for i in range(len(first_part)):
            if first_part[i] != second_part[-(i+1)]:
                return False
        return True
        