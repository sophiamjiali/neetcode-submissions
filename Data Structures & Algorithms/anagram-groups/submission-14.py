class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Dictionaries cannot be used as keys; use an array to 
        # represent character occurrences because they can be
        # directly asserted

        map = dict()
        for s in strs:
            s_key = self.computeKey(s)

            if s_key in map:
                map[s_key].append(s)
            else:
                map[s_key] = [s]

        results = []
        for key in map:
            results.append(map[key])

        return results



    def computeKey(self, s: str) -> tuple:
        # Returns an array representing each character's occurrence
        # in string s, from a to z.

        # Subtract the 'a' ASCII to start index from zero
        a_key = ord('a')

        map = [0] * 26
        for char in s:
            key = ord(char) - a_key
            map[key] += 1
        return tuple(map)
