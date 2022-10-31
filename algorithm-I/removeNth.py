from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    temp = head
    length = 0
    
    while temp:
        temp = temp.next
        length += 1
        
    if length == n : 
        return head.next
    
    temp = head
    for i in range(length-n):
        if i < length - n - 1: temp = temp.next
    temp.next = temp.next.next
    return head

numbers = [1,2,3,4,5]
head = ListNode()
sll = head 
i = 0
while i < len(numbers) :
    if i == 0 : head.val = numbers[i]
    else :
        temp = ListNode(numbers[i])
        head.next = temp
        head = head.next
    i += 1
    
xtemp = remove_nth_from_end(sll,2)
while xtemp :
    print(xtemp.val,end=" ")
    xtemp = xtemp.next