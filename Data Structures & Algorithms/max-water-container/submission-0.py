class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_capacity = 0 
        left_wall, right_wall = 0, len(heights)-1

        while left_wall < right_wall:
            capacity = min(heights[left_wall],heights[right_wall]) * (right_wall - left_wall)

            if capacity > max_capacity:
                max_capacity = capacity
                if heights[left_wall] > heights[right_wall]:
                    right_wall -= 1
                
                elif heights[left_wall] < heights[right_wall]:
                    left_wall += 1
                
                else:
                    right_wall -= 1 
            
            else:
                if heights[left_wall] > heights[right_wall]:
                    right_wall -= 1
                
                elif heights[left_wall] < heights[right_wall]:
                    left_wall += 1
                
                else:
                    right_wall -= 1 

        return max_capacity

                
        