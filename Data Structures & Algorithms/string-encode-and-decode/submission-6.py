class Solution:

    def encode(self, strs: List[str]) -> str:

        # - most likely needs to be in O(n)
        # - naively, delimit, but may occur in a string
        # - thus, use length of string as well, with a break
        # - only track length; don't need to worry about randomly
        #   finding a number, because always start at the beginning
        # - can't assume the length of the string is a single digit

        encoded_string = ""

        for s in strs:
            encoded_string += f"{len(s)}#{s}"

        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_strs = []

        i = 0
        while i < len(s):
            
            # Find the end of the digit
            j = i
            while s[j] != "#": 
                j += 1

            # Extract the length of the string
            s_len = int(s[i:j])

            # Extract the string
            i = j + 1
            j = i + s_len

            decoded_strs.append(s[i:j])

            # Point i to the char after the end of the string
            i = j

        return decoded_strs

