class Solution(object):
    def twoSum(self, numbers, target):
        a=0
        b= len(numbers)-1
        while a<b:
            sum= numbers[a]+numbers[b]
            if sum== target:
                return [a+1, b+1]
            elif sum > target:
                b= b-1
            else:
                a= a+1
        