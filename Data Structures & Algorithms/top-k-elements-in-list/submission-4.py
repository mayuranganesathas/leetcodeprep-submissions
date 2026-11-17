class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #key is the number / char, value is the frequency
        freqMap = {} 
        result = []


        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            bucket[freq].append(num)


        
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
                
                


        




        #we need the frequency from a list. so we itearte through and get a frequency map
        #iterate through the frequency map and rebuild into a list based on priority
        # stop iterating when we reach the k val