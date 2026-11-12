class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in map: return [map[compliment], i]
            
            if nums[i] in map: continue 
            map[nums[i]] = i
        








    
    #brute force is to go through every index, and compare with the rest of the indexes in the array to match with the target 
    #a clever way t ogo about this is that we know the end goal number, and another half of the equation, ie x + index = target
    # instead we can go through each index and store the value in a map
    # then we check if the array has a compliment ie. if we isolate for x, we can see if its in the map, if not - just keep going through the array
 # we want to store as key: nums[i] value: i
# we dont worry about duplicates cause we store the earliest value in the index, and the problem guaruntees one pair





        