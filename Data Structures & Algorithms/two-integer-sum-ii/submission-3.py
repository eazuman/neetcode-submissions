class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)-1
        n = 0

        while n < l :
            m = n+1
            while m < l+1 :
                print("numbers[n] and  numbers[l]",numbers[n] ,numbers[n+1] )
                if numbers[n] + numbers[m] == target:
                    return [n+1,m+1]
                m += 1
            n += 1
            

