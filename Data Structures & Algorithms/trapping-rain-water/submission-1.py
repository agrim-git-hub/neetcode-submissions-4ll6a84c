class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = right_max = 0
        left = 0
        right = n-1
        collected_water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= left_max:
                    left_max = height[left]

                else:
                    collected_water += left_max- height[left]

                left += 1
            
            else:

                if height[right] >= right_max:
                    right_max = height[right]

                else:
                    collected_water += right_max- height[right]
                    
                right -= 1
        
        return collected_water


            