
import sys



def oneToOneMapping(s1: str, s2: str) -> bool:
    if (len(s2) < len(s1)):
        return False
    
    # dictionary to store mappings
    mapDict = {}

    numMapping = len(s1)
    
    # iterate over 2 strings
    for index in range(numMapping):
        key = s1[index]
        value = s2[index]
        if mapDict.get(key) is None:
            mapDict[key] = value
        elif mapDict[key] != value:
            return False
    
    return True


if __name__ == '__main__':
    # read string inputs
    s1 = sys.argv[1]
    s2 = sys.argv[2]

    # print result output
    if oneToOneMapping(s1, s2):
        print('true')
    else:
        print('false')
