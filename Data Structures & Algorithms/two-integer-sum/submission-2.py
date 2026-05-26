class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        i = 0 
        j = 0 

        for i in range(0, len(nums)): 
            result = []
            match =  target - nums[i]
            result.append(i) 
        # i = i 

            if match in nums: 
                for j in range(i+1, len(nums)):
                    if nums[j] == match: 
                        # j = j 
                        result.append(j)
                        return result

        
