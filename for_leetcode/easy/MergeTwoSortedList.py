# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        total_list = ListNode()
        current = total_list
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return total_list.next
        # Men yangi ro'yxat yarataman
        # Men ikkala ro'yxatni ham oxiriga yetgunicha ishlayman:

        # AGAR list1dagi son list2dagidan kichik bo'lsa:
        #     Men list1dagi sonni olib yangi ro'yxatga qo'shaman
        #     List1ni keyingi soniga o'taman
        
        # YOKI AGAR list2dagi son kichik bo'lsa:
        #     Men list2dagi sonni olib yangi ro'yxatga qo'shaman
        #     List2ni keyingi soniga o'taman

        # Agar list1da son qolgan bo'lsa:
        #     Men qolgan barcha sonlarni yangi ro'yxatga qo'shib qo'yaman

        # Agar list2da son qolgan bo'lsa:
        #     Men qolgan barcha sonlarni yangi ro'yxatga qo'shib qo'yaman

# type: ignore