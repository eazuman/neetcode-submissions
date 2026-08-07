class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        print("Test nums", nums)
        k = 0
        l = len(nums)
        r = 0
        for r in range(l):
            if nums[r] != val:
                nums[k] = nums[r] 
                k += 1
            r += 1
        return k



            


        