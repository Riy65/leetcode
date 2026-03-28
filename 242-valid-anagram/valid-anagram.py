class Solution(object):
    def isAnagram(self, s, t):
        dict={}
        for ch in s:
            if ch in dict:
                dict[ch]+=1
            else:
                dict[ch]=1
        
        for ch in t:
            if ch in dict and dict[ch]>0:
                dict[ch]-=1
                if dict[ch]==0:
                    del dict[ch]
            else:
                return False
    
        if not dict:
            return True
        else:
            return False
