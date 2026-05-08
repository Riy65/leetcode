class Solution(object):
    def majorityElement(self, nums):
        dict={}
        n= len(nums)
        for num in nums:
            if num in dict:
                dict[num]+=1
                if dict[num]> n/2:
                    return num
            else:
                dict[num]=1
                if dict[num]> n/2:
                    return num
        
      
        