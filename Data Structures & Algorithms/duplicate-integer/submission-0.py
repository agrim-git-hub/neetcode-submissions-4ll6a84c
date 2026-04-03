class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #we best solve this sum using hashmaps. using set
        return (len(nums) != len(set(nums)))