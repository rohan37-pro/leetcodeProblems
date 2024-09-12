# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head) :
        if head==None or head.next==None:
            return head
        cur = head
        nxt = head.next
        while nxt:
            hcf = self.gcd(cur.val, nxt.val)
            cur.next = ListNode(val=hcf, next=nxt)
            cur = nxt
            nxt = nxt.next
        return head
    
    def gcd(self, a, b):
        if a%b==0:
            return b
        else :
            return self.gcd(b, a%b)


obj = Solution()

headlist = [7]

head = ListNode(headlist[0])
cur = head
for i in headlist[1:]:
    cur.next = ListNode(i)
    cur = cur.next

output = obj.insertGreatestCommonDivisors(head)
while output:
    print(output.val, end=' ')
    output = output.next
print()