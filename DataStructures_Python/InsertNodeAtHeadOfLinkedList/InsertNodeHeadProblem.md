## Insert a node at the head of a linked list

Given a pointer to the head of a linked list, insert a new node before the head. The nex  value in the new node should point to head and the data value should be replaced with a given value. Return a reference to the new head of the list. The head pointer given may be null meaning that the initial list is empty.

#### Function Description

Complete the function insertNodeAtHead in the editor below.

insertNodeAtHead has the following parameter(s):

    SinglyLinkedListNode llist: a reference to the head of a list
    data: the value to insert in the data field of the new node

#### Input Format

The first line contains an integer n, the number of elements to be inserted at the head of the list.
The next n lines contain an integer each, the elements to be inserted, one per function call. 