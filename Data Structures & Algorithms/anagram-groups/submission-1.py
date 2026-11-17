class Solution:

    def hashMap(self, s: str) -> str:
        counts = [0] * 26

        for c in s:
            counts[ord(c) - ord('a')] += 1

        return "#".join(map(str, counts))



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) is None: return []
        #Create hash map to store by key: string has, value: an array to push into
        stringMap = {}
        result = []

        #go through the array and store in the hash map

        for i in range(len(strs)):
            strHash = self.hashMap(strs[i])
            if strHash not in stringMap:
                stringMap[strHash] = []

            stringMap[strHash].append(strs[i])

        #iterate through the map and push it into a final array
    
        return list(stringMap.values())



        #this is to group by frequency of characters: ie. deconstructed anagrams just need to merit the same characters and the same amount of characters to do that 
        #instead of doing nested loops and comparing with each other string (after being sorted) and pushing all that are similar into an array we can...
     #what if we use a map, convert into a string hash as the key. Then the valeus is an array of thhose with the same key / string hash 
     # to determine string hash we can use the similarity of a-z letters (lower case hash)