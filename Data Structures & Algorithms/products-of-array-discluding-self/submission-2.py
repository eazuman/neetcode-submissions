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
        product = 1
        for i in range(s):
            if i == 0 :
                product = 1
            else:
                product = nums[i-1]*product
            left_list.append(product)

        for j in range(s-1,-1,-1):
            print("j is:",j,nums[j])
            if j == s-1 :
                product = 1
            else:
                product = nums[j+1]*product
            right_list.append(product)
        right_list.reverse()


        for l in range(s):
            final = right_list[l]*left_list[l]
            final_list.append(final)
        return final_list
