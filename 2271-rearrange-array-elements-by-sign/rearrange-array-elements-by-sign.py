class Solution(object):
    def rearrangeArray(self, nums):
        result=[]
        pos= 0
        neg= 1
        for i in range(len(nums)):
            if nums[i]>0:
                result.insert(pos, nums[i])
                pos= pos+2
            else:
                result.insert(neg, nums[i])
                neg= neg+2
        return result

     
        