class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # O(n) space

        max_length = 0

        for num in num_set:
            # CHECK: Is 'n' the start of a sequence?
            if (num-1) not in num_set:
                # BUILD: Follow the sequence upward
                current_length = 1
                while (num + current_length) in num_set:
                    current_length +=1
                
                max_length = max(max_length, current_length)

        return max_length
