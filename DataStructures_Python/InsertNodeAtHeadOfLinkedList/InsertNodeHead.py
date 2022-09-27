

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
# The head is the back of the list
def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)
    node.next = llist
    llist_head = node
    
    # llist.head is what is passed in
    return llist_head

