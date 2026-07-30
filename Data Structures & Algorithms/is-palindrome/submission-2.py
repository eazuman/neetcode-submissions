class Solution:
    def isPalindrome(self, s: str) -> bool:
        print("String is:",s)
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned = cleaned+char.lower()
        print("Final char",cleaned)
        l = len(cleaned)-1
        n = 0

        while n < l:
            if cleaned[n] != cleaned[l]:
                return False
            else:
                 n += 1
                 l -= 1
        return True

             
