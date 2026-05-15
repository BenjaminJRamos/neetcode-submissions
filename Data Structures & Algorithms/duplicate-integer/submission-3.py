class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        haveSeen = set()

        for i in nums:
           if i in haveSeen:
                return True
           haveSeen.add(i)

        return False 