class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []

        def solve(index, target, subset):

            # Target achieved
            if target == 0:
                ans.append(subset[:])
                return

            # Out of bounds
            if index == len(candidates):
                return

            # TAKE
            if candidates[index] <= target:
                subset.append(candidates[index])
                solve(index, target - candidates[index], subset)
                subset.pop()

            # NOT TAKE
            solve(index + 1, target, subset)

        solve(0, target, [])
        return ans
        