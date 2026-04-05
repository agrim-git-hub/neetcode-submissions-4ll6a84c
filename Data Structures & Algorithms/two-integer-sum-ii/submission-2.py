class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_knob, right_knob = 0, len(numbers)-1

        while left_knob < right_knob:
            s = numbers[left_knob] + numbers[right_knob]
            if s == target:
                return [left_knob + 1, right_knob + 1]
            elif s < target:
                left_knob += 1
            else:
                right_knob -= 1
        