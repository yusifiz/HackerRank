def deleteNode(head, position):
    if position == 0:
        return head.next
    current = head
    for i in range(position-1):
        current = current.next
    current.next = current.next.next
    
    return head
