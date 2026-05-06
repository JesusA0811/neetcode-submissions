class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #empty dict key:value

        #loopthrough every index in nums
        for i in range(len(nums)):
            hashMap[nums[i]] = i
    
        for i in range(len(nums)):
            #remaing amount to make target
            y = target - nums[i]
            #y has to be in the dict and can't be the same index
            if y in hashMap and hashMap[y] != i:
                return [i,hashMap[y]]
                
        