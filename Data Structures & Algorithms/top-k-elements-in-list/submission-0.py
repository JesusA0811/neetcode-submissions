class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1

        sortedItems = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        return [sortedItems[i][0] for i in range(k)]
