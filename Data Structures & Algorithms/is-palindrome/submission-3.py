class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)-1
        n = 0

        while n < l:
            while n < l and not s[n].isalnum():
                n += 1
            while n < l and not s[l].isalnum():
                l -= 1    
            print("s[n].lower and s[l",s[n],s[l])    
            if s[n].lower() != s[l].lower():
                return False
            n += 1
            l -= 1
        return True

             
