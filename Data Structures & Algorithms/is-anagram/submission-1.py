class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array1 = [0] * 26
        array2 = [0] * 26
        
        for char in s:
            c = ord(char) - ord('a')
            array1[c] += 1
        
        for char in t:
            c = ord(char) - ord('a')
            array2[c] += 1
        
        return array1 == array2
