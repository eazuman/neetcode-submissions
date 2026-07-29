class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # s = len(nums)
        # result_list = []
        # for i in range(s):
        #     product = 1
        #     for j in range(s):
        #         if j != i:
        #             product = product*nums[j]
        #     result_list.append(product)
        # return result_list
        s = len(nums)
        left_list = []
        right_list = []
        final_list = []
        product_left = 1
        product_right = 1
        for i in range(s):    
            left_list.append(product_left)
            product_left = nums[i]*product_left

        for j in range(s-1,-1,-1):
            right_list.append(product_right)
            product_right = nums[j]*product_right
        right_list.reverse()


        for l in range(s):
            final = right_list[l]*left_list[l]
            final_list.append(final)
        return final_list
