#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.data = None
        self.next = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        data = node_data

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data), end=sep)

        node = node.next

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def mergeLists(head1, head2):
    '''
    merges 2 lists
    '''
    print('Hi')
    merged = SinglyLinkedList()
    print('List created')
    print_singly_linked_list(head1, ' ')
    print_singly_linked_list(head2, ' ')
    iteration = 0
    while head1.next and head2.next:
        print()
        print('Iteration ', iteration)
        if head1 == None and head2 != None:
            print('Head1 None')
            value = head2.data
            merged.insert_node(value)
            print(f'Insert {value}')
            head2 = head2.next
            print(f'Next element is {head2.data}')
            #print_singly_linked_list(merged, ' ')
        elif head2 == None and head1 != None:
            print('Head2 None')
            value = head1.data
            merged.insert_node(value)
            print(f'Insert {value}')
            head1 = head1.next
            print(f'Next element is {head1.data}')
            #print_singly_linked_list(merged, ' ')
        elif head1.data <= head2.data:
            print('Data1 <= Data2')
            value = head1.data
            merged.insert_node(value)
            print(f'Insert {value}')
            head1 = head1.next
            if head1!=None:
                print(f'Next element is {head1.data}')
            #print_singly_linked_list(merged, ' ')
        else:
            print('Data2 < Data1')
            value = head2.data
            merged.insert_node()
            print(f'Insert {value}')
            head2 = head2.next
            if head2 != None:
                print(f'Next element is {head2.data}')
            print_singly_linked_list(merged, ' ')
        iteration += 1
        print('============')
    return merged
    

if __name__ == '__main__':
    llist1 = SinglyLinkedList()
    l1 = [1, 2, 3]
    llist2 = SinglyLinkedList()
    l2 = [2, 3, 4]
    for l in l1:
        llist1.insert_node(l)
            
    for l in l2:
        llist2.insert_node(l)


    llist3 = mergeLists(llist1.head, llist2.head)

    print_singly_linked_list(llist3, ' ')

