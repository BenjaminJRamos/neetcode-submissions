class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        result = {}
        for i in strs:

            key = "".join(sorted(i))

        
            if key in result:
                result[key].append(i)
            else:  
                result[key] = [i]

        print("this is the result", list(result.values()))
        return list(result.values())
         
          

            # add logic to handle the checking if any other elements in the array
            # are anagroms and then remove it from the array



        return result 