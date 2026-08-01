class Solution(object):
    def permute(self, nums):
        ans=[]
        def solve(index):
            if index==len(nums):
                ans.append(nums[:])
                return
            for i in range(index,len(nums)):
                nums[index],nums[i]=nums[i],nums[index]
                solve(index+1)
                nums[index],nums[i]=nums[i],nums[index]
        solve(0)
        return ans