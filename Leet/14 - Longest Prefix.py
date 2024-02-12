class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        o = ""
        min = 999
        inx = 0
        for i in range(0, len(strs)):
            if(len(strs[i]) == 0):
                return o
            if(i != len(strs)-1):
                y = strs[i]
                z = strs[i+1]
                if(y != "" and z != ""):
                    if(y[0] != z[0]):
                        return o
                else:
                    return o
            if(len(strs[i]) < min):
                min = len(strs[i])
                inx = i
        o = strs[inx]
        p = ""
        for i in range(0, len(o)):
            result = all(s[i] == o[i] for s in strs)
            if(result == True):
                p += o[i]
            if(result == False):
                break
        return p