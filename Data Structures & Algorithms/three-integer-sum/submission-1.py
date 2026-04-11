class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for control_pointer in range(len(nums)):
            if nums[control_pointer] > 0:
                break

            if control_pointer > 0 and nums[control_pointer] == nums[control_pointer-1]:
                continue
            
            inner_left = control_pointer + 1
            inner_right = len(nums) - 1

            while inner_left < inner_right :

                sum = nums[control_pointer] + nums[inner_left] + nums[inner_right]

                if sum > 0:
                    inner_right -= 1
                elif sum < 0:
                    inner_left += 1
                else:
                    result.append([nums[control_pointer],nums[inner_left],nums[inner_right]])
                    inner_right -= 1
                    inner_left += 1

                    while nums[inner_left] == nums[inner_left-1] and inner_left < inner_right:
                        inner_left += 1

                    while nums[inner_right] == nums[inner_right + 1] and inner_left < inner_right:
                        inner_right -= 1

        return result