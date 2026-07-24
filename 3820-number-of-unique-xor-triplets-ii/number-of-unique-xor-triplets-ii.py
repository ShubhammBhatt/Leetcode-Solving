class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        unique_nums = list(set(nums))
        
        pairs = set()
        for i in range(len(unique_nums)):
            for j in range(i, len(unique_nums)):
                pairs.add(unique_nums[i] ^ unique_nums[j])
                
        triplets = set()
        for p in pairs:
            for x in unique_nums:
                triplets.add(p ^ x)
                
        return len(triplets)