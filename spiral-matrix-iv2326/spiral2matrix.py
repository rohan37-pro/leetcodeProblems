# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m, n, head):
        nl = 0
        nr = n-1
        mt = 0
        mb = m -1
        dx = 0
        dy = 0
        matrix = [[-1]*n for i in range(m)]
        while head:
            if dx==0 and dy==0:
                for i in range(nl, nr+1):
                    if head :
                        matrix[mt][i] = head.val
                        head = head.next
                    else:
                        return matrix
                    
                dy=-1
                mt += 1
            if dx==0 and dy==-1:
                for i in range(mt, mb+1):
                    if head :
                        matrix[i][nr] = head.val
                        head = head.next
                    else:
                        return matrix
                dx=-1
                nr -= 1
            if dx==-1 and dy==-1:
                for i in range(nr, nl-1, -1):
                    if head :
                        matrix[mb][i] = head.val
                        head = head.next
                    else:
                        return matrix
                dy=0
                mb -= 1
            if dx==-1 and dy==0 :
                for i in range(mb, mt-1, -1):
                    if head :
                        matrix[i][nl] = head.val
                        head = head.next
                    else:
                        return matrix
                dx=0
                nl += 1
        return matrix



# m = 6
# n = 7
# head_list = [3,0,2,6,8,1,7,9,4,2,5,5,0]

# head = ListNode(head_list[0])
# cur = head
# for i in head_list[1:]:
#     cur.next = ListNode(i)
#     cur = cur.next

# obj = Solution()
# print(obj.spiralMatrix(m, n, head))