class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for i in strs:
            # Place the delimiter after the length to handle multi-digit lengths
            code = str(len(i)) + "#"
            enc_str += code 
            enc_str += i
        print("THIS IS THE ENC_STR ", enc_str)
        return enc_str

    def decode(self, s: str) -> List[str]:
        dec_arr = []
        index = 0 
        while(index < len(s)):
            # Find the next delimiter to determine where the length string ends
            j = index
            while s[j] != '#':
                j += 1
            
            str_len = int(s[index:j])
            # Extract the substring based on the parsed length
            substring = s[j + 1 : j + 1 + str_len]
            dec_arr.append(substring)
            
            # Move index to the start of the next encoded block
            index = j + 1 + str_len
        return dec_arr