class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in nums and nums.index(diff) != i:
        #         final = [i,nums.index(diff)]
        #         return sorted(final)
        # for i, n in enumerate(nums):
        #     if i == len(nums):
        #         return
        #     for j in range(i+1,len(nums)):
        #         print("i and n is",i,n)
        #         print("j and range is",j,nums[j])
        #         if n+nums[j] == target:
        #             print("the numbers are:",n,nums[j])
        #             return [i,j]
        map_dict = {}
        for i, n in enumerate(nums):
            print("for loop",i,n)
            diff = target - n
            print("for loop vars and diff",i,n,diff)
            if n in map_dict:
                print("Found diff in map_dict",n)
                return [map_dict[n],i]
            else:
                map_dict[diff] = i
            print("map_dict",map_dict)
