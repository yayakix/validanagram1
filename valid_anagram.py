class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapS = {}
        mapT = {}
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            currValS = s[x]
            currValT = t[x]
            mapS[currValS] = mapS.get(currValS, 0) + 1
            mapT[currValT] = mapT.get(currValT, 0) + 1
        for c in mapS:
            if c not in mapT:
                return False
            if mapS[c] != mapT[c]:
                return False
        return True
