

#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    
    node = SinglyLinkedListNode(data)
    
    # Create pointer whilst preserving head
    current = llist
    # Move pointer until next postion is where we want the item
    for i in range(position-1):
        current = current.next
    
    # Store value to link new node to
    next_val = current.next
    
    current.next = node
    node.next = next_val
    
    return llist
    

