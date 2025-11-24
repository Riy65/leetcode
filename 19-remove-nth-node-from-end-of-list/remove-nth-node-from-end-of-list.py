# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count =0
        temp= head
        while temp :
            count+=1
            temp=temp.next
        
        result= count- n
        if result==0:
            newhead= head.next
            return newhead
        temp2= head
        
    
        while temp2:
            result-=1
            if result==0:
                break
            temp2= temp2.next
        temp2.next=temp2.next.next
        return head
        
            
        
            
    
            
        
            
        