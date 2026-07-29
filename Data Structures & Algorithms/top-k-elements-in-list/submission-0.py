class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_dict = {}
        for item in nums:
            if item in map_dict:
                map_dict[item] += 1
            else:
                map_dict[item] = 1
        print("map_dict final",map_dict)
        items_list = sorted(map_dict.items(),key=lambda pair:pair[1],reverse=True)
        print("items_list",items_list[0:k])
        final_list = []
        for n in items_list[0:k]:
            print(n[0])
            final_list.append(n[0])
        return final_list