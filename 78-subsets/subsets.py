class Solution(object):
    def subsets(self, nums):
        ans = []
        def solve(index, subset):
            if index == len(nums):
                ans.append(subset[:])
                return
            subset.append(nums[index])
            solve(index + 1, subset)
            subset.pop()
            solve(index + 1, subset)
        solve(0, [])
        return ans
     































        
    
        