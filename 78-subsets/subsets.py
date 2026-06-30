class Solution(object):
    def subsets(self, nums):
        ans = []

        def solve(index, subset):
            if index == len(nums):
                ans.append(subset[:])
                return

            # Take
            subset.append(nums[index])
            solve(index + 1, subset)

            # Backtrack
            subset.pop()

            # Not Take
            solve(index + 1, subset)

        solve(0, [])
        return ans
     































        
    
        