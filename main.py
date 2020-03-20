class Solution:
    def oneToOneMapping(self, s1: str, s2: str) -> bool:
        # dictionary to store mappings
        mapDict = {}

        if (len(s2) < len(s1)):
            return False

        numMapping = len(s1)
        
        # iterate over 2 strings
        for index in range(numMapping):
            key = s1[index]
            value = s2[index]
            if mapDict[key] is None:
                mapDict[key] = value
            elif mapDict[key] != value:
                return False
        
        return True