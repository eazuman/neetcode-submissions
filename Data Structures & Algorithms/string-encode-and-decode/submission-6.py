class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ''
        for item in strs:
            print(item)
            l = len(item)
            newstr =  str(l) +'#'+item
            print("newstr",newstr)
            final_str= final_str+newstr
        print("final_str",final_str)
        return final_str


    def decode(self, s: str) -> List[str]:
        my_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1                       

            length = int(s[i : j]) 

            start = j + 1                   
            piece = s[start : start + length]
            my_list.append(piece)

            i = start + length                 
        return (my_list)
