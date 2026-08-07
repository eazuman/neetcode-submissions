class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        print("Test nums", nums)
        expectedNums = []
        for item in nums:
            if item != val:
                expectedNums.append(item)
        print("nums",expectedNums)
        k = len(expectedNums)
        nums[:] = expectedNums

        return k



            


        