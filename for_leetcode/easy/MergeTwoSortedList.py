# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
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