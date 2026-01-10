#class ListNode(object):
    
     #def __init__(self, val=0, next=None):
            #self.val = val
            #self.next = next

class reverse:
    def rev(self,head):
        curr = head
        prev = None
        
        while curr:
            
            nxt = ListNode(curr.val)
            nxt.next = prev
            prev = nxt
            curr = curr.next
            
        return prev

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1r = l1 #reverse().rev(l1)
        l2r = l2 #reverse().rev(l2)
        carry =0
        prev = None

        while l1r or l2r or carry != 0:

            x = l1r.val if l1r else 0
            y = l2r.val if l2r else 0

            total = (x+y + carry)%10
            carry = (x+y + carry)//10

            l3r = ListNode(total)
            l3r.next = prev
            prev = l3r

            if l1r:
                l1r = l1r.next
            if l2r:
                l2r = l2r.next

        ans = reverse().rev(prev)
        
        return ans
        
        