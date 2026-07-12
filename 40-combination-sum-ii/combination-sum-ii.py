class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans=[]
        def solve(index, target, subset):
            if target==0:
                ans.append(subset[:])
                return
            if index==len(candidates):
                return
            if candidates[index]<=target:
                subset.append(candidates[index])
                solve(index+1, target-candidates[index], subset)
                subset.pop()

            while(index+1<len(candidates)and candidates[index]==candidates[index+1]):
                index=index+1
            solve(index+1, target, subset)
        solve(0,target,[])
        return ans
   
        