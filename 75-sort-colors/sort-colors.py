class Solution(object):
    def sortColors(self, nums):
        a=0
        b=0
        c=0
        for num in nums:
            if num==0:
                a=a+1
            elif num==1:
                b=b+1
            else:
                c=c+1
        i=0
        for _ in range(a):
            nums[i]=0
            i=i+1
        for _ in range(b):
            nums[i]=1
            i=i+1
        for _ in range(c):
            nums[i]=2
            i=i+1
        return nums
      
        