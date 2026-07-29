class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = len(nums)
        result_list = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product = product*nums[j]
            result_list.append(product)
        return result_list

                
            