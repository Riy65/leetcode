class Solution(object):
    def myAtoi(self, s):
        k = s.lstrip()
        n= len(k)
        result=0
        a=1
        b=0
       
        if not k:
            return 0
        elif k[0]=='-':
            
            while a<n and k[a].isdigit():
                result= result*10 + int(k[a])
                a+=1
            result= result*-1
            if result<= -2**31:
                return -2**31
            else: 
                return result
        elif k[0]=='+':
            while a<n and k[a].isdigit():
                result= result*10 + int(k[a])
                a+=1
            if result>= 2**31 -1:
                return 2**31 -1
            else:
                return result
        else:
            while b<n and k[b].isdigit():
                result= result*10 + int(k[b])
                b+=1
            if result>= 2**31 -1:
                return 2**31 -1
            else:
                return result
        
            