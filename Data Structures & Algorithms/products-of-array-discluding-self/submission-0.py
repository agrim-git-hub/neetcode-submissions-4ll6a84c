class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #for this we need to use the classic prefix/suffix logic to solve this question
        prefix = 1
        size=len(nums)
        l1=[1]*size
        for i in range(size):
            l1[i] = l1[i]*prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(size-1,-1,-1):
            l1[i] = l1[i]*suffix
            suffix *= nums[i]
        return l1