class Solution(object):
    def maxArea(self, height):
        a=0
        b=len(height)-1
        result=0
        while a!=b:
            area= (b-a)* min(height[a],height[b])
            result= max(area, result)
            if height[a]> height[b]:
                b=b-1
            else:
                a=a+1
        return result
        

        