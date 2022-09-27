# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    
    # If list is empty -> insert node
    if head is None:
        head = node
        return head
        
    # Traverse list to the tail until it points to None
    current = head
    
    while current.next is not None:
        current = current.next
        
    # Currently goes right to the back every time
    current.next = node 
        
    return head
    
    