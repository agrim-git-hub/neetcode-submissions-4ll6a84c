class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_knob, right_knob = 0, len(numbers)-1

        while left_knob < right_knob:
            if numbers[left_knob] + numbers[right_knob] == target:
                return [left_knob+1,right_knob+1]
            else:
                if numbers[left_knob] + numbers[right_knob] < target:
                    left_knob += 1
                if numbers[left_knob] + numbers[right_knob] > target:
                    right_knob -= 1
        