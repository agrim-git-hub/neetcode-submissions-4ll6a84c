class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we can use a hashmap, to map the number in nums to its index. while iterating through nums, if the difference exists in the hashmap, we return the current index and also the index from the element retrieved from the hashmap
        sample_hash = {}
        for i in range(len(nums)):
            if (target - nums[i]) in sample_hash:
                return[sample_hash[target - nums[i]],i]

            sample_hash[nums[i]] = i 