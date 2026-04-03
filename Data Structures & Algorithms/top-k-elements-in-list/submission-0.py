class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies (O(n))
        dictionary = {}
        for i in nums:
            dictionary[i] = dictionary.get(i,0)+1
        
        # 2. Bucket Sort: Index is frequency, value is list of numbers (O(n))
        buckets = [[] for _ in range(len(nums)+1)]
        for number, frequency in dictionary.items():
            buckets[frequency].append(number)
        
        # 3. Collect the top K (O(n))
        final_list = []
        # Iterate backwards from the highest possible frequency
        for i in range(len(buckets)-1, 0, -1):
            for number in buckets[i]:
                final_list.append(number)
                if len(final_list)==k:
                    return final_list
        
        