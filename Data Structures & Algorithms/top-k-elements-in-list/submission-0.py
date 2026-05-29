class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = []

    # Make a frequency counter using a dictionary:
        freq = defaultdict(list)
        for i in nums: 
            freq[i].append(i)
        print("THIS IS FREQ:", freq)

    # Add tp the result array depending on the k inputs 
        while(k > 0):

            longest_key = max(freq, key=lambda k: len(freq[k]))
            result.append(longest_key)
            #removes/clears the values of the longest key: 
            freq[longest_key] = []
            k -= 1 
            print("K:", k, " RESULT:", result)
        return result