class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        contains = {} # changed it to an dictionary for efficiency instead of a set for duplicates 

        # filling the dictionary(hashmap) with content 
        for i in s:
            contains[i] = contains.get(i, 0) + 1 # using get() is the safe way to add/getting a value without resulting in an error if there is no value there yet

        for i in t:
        
            if contains.get(i, 0) == 0:
                return False 

            contains[i] -= 1 

        return True