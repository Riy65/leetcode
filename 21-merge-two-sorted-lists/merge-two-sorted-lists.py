# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp1= list1
        temp2= list2
        ans= ListNode(0)
        head= ans
        

        while temp1 and temp2:
            if temp1.val< temp2.val:
                head.next= temp1
                temp1=temp1.next
                head= head.next
            elif temp1.val== temp2.val:
                head.next = temp1
                temp1 = temp1.next
                head = head.next
                head.next = temp2
                temp2 = temp2.next
                head = head.next
            else:
                head.next = temp2
                temp2 = temp2.next
                head = head.next

        head.next = temp1 if temp1 else temp2
        return ans.next

        
        