# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums, head):
        nums.sort()
        f = True
        while f:
            if head.val in nums:
                head = head.next
            else:
                f=False
        prev = head
        current = None
        if head.next :
            current = head.next
        if current!=None:
            while current.next:
                if self.find_element(current.val, nums):
                    prev.next = current.next
                    current = current.next
                else:
                    prev = current
                    current = current.next
        if current and self.find_element(current.val, nums):
            prev.next = None
        return head
    
    def find_element(self, val, nums):
        l = 0
        r = len(nums)-1
        if val==nums[l] or val==nums[r]:
            return True
        while r-l>1:
            m = (l+r)//2
            if val==nums[m]:
                return True
            if val>nums[m]:
                l = m
            if val<nums[m]:
                r = m
        return False
        

nums = [1]
data = [1,2,1,2,1,2]

head = ListNode(val=data[0])
current = head
for i in data[1:]:
    current.next = ListNode(val=i)
    current = current.next

obj = Solution()
mhead = obj.modifiedList(nums, head)
while mhead:
    print(mhead.val)
    mhead = mhead.next