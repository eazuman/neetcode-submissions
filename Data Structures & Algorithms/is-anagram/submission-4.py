class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        s_map = {}
        t_map = {}
        for ss,tt in zip(s,t):
            if ss in s_map:
                s_map[ss] += 1
            else:
                s_map[ss] = 1    
            if tt in t_map:
                t_map[tt] += 1   
            else:
                t_map[tt] = 1    
        print("s_map",s_map)
        print("t_map",t_map)
        if s_map == t_map:
            return True
        return False
