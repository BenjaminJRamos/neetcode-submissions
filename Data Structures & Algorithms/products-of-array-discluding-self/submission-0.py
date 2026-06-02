class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        prd_woo = 1 
        first = True 
        for i in nums: 

            if i == 0: 
                if first == True:
                    print("FIRED FIRST")
                    prd_woo = product 
                    product *= i 
                    first = False
                else: 
                    print("FIRED")
                    prd_woo *= i 
                    product *= i  
            else: 
                product *= i
                prd_woo *= i  
            print("PRD_WOO", prd_woo, "PRODUCT:", product)


        result = []
        for i in nums:
            if i == 0:
                inp = prd_woo
            else:
             inp = product // i
            result.append(inp)
        return result 
            