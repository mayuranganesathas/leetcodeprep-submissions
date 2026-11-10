class Solution:


    def createStringHash(self, s:str) -> str:
        hash = {}
        # Helper function to create this
        for i in range(len(s)):
            char = s[i]
            hash[char] = hash.get(char, 0) + 1
        return hash



    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if s == t:
            return True


        #create 1st string hash
        sHash = self.createStringHash(s)

        #create 2nd string hash
        tHash = self.createStringHash(t)


        if sHash == tHash: return True

        return False


    


 
        


    

# anagram is defined as the same characters 
# that means # of letters needs to be the same
# if both have 0 false as well
# can be out of order, so you wont really knwo till the end
# you can put it into a datastructure and scan or put it into order and then scan 
# prior may be O(n2), latter can be o (nlogn). '
# you can put into a hash and compare - where we use ascii code numbers to create a hash
#the hash can be directly compared after, without requiring a new scan 



