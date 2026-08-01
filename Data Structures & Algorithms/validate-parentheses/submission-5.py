class Solution:
    def isValid(self, s: str) -> bool:
        print("String",s)
        c = {')':'(', '}' : '{', ']' : '['}
        test_set = []
        for n in s:
            if n in ('(','{','[' ):
                print("OPenign bracket",n)
                test_set.append(n)
            if not test_set:
                return False
            if n in (')','}',']' ) :
                print("closing bracket", n, c[n])             
                last = test_set.pop()
                if last != c[n]:
                    print("no match found match")
                    print("test_set.pop after ",test_set)
                    return False
                print("test_set.pop 1 loop ",test_set)
        if test_set:
            return False
        return True
