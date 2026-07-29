class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict = {}
        for i, item in enumerate(strs):
            new_item = "".join(sorted(item))
            if new_item in map_dict:
                map_dict[new_item].append(item)
            else:
                map_dict[new_item] = [item]
        return list(map_dict.values())

