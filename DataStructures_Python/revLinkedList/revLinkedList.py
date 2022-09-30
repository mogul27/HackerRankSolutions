#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# More efficient way by setting pointer.next = prev

def reverse(llist):
    
    llist_values = []
    
    pointer = llist
    
    while pointer != None:
        llist_values.append(pointer)
        pointer = pointer.next
    
    llist_values.reverse()
    
    for i in range(len(llist_values[:-1])):
        # Set each value to point to the next unless last
        llist_values[i].next = llist_values[i+1]
    
    llist_values[-1].next = None
    
    return llist_values[0]
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()