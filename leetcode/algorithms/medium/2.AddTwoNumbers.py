# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class List_to_Linked:
    def __init__(self, l: list):
        self.head = ListNode(l[0])
        current = self.head
        for val in l[1:]:
            current.next = ListNode(val)
            current = current.next


class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in REVERSE order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, 
    except the number 0 itself.

    """
    def addTwoNumbers(self, l1: Optional([ListNode]), l2: Optional([ListNode])) -> Optional([ListNode]):
        result = ListNode(0)
        tail = result
        # to keep a carry, for example 9 + 7 = 16, carry will be 1
        carry = 0
        
        while (l1 or l2 or carry != 0):
            # list numbers are in reverse order, so we sum from the head to tail

            # save values
            l1_num = l1.value if l1 else 0
            l2_num = l2.value if l2 else 0

            # move pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # sum 2 numbers and carry if available
            sum = l1_num + l2_num + carry

            # get 2 digits: carry returns floor division by 10, ot and 
            # create a new ListNode with modulo 10 value and append to the tail  
            carry = sum // 10
            tail.next = ListNode(sum % 10)
            # update tail pointer
            tail = tail.next
        # not to return the leading 0 we return the 2nd value
        return result.next
