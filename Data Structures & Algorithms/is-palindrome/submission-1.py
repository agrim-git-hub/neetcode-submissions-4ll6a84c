class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, end = 0, len(s)-1
        while front < end:

            while front < end and s[front].isalnum() != True: 
                front += 1

            while front < end and s[end].isalnum() != True:
                end -= 1

            if s[front].lower() != s[end].lower():
                return False

            front += 1
            end -= 1

        return True
        