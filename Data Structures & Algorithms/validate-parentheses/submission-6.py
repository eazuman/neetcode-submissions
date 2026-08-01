class Solution:
    def isValid(self, s: str) -> bool:
        print("String",s)
        c = {')':'(', '}' : '{', ']' : '['}
        test_set = []
        for n in s:
            if n in ('(','{','[' ):
                test_set.append(n)
            if not test_set:
                return False
            if n in (')','}',']' ) :
                last = test_set.pop()
                if last != c[n]:
                    return False
        if test_set:
            return False
        return True
