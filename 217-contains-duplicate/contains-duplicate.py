class Solution(object):
    def containsDuplicate( self, nums):
        numdict={}
        for i in nums:
            if i in numdict:
                return True
            else:
                numdict[i]=1
            
            
        return False



       
        