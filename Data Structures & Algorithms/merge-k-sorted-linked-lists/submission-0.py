# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        interval = 1
        if not lists:
            return None
        k = len(lists)
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if (i+1) < len(lists):
                    list2 = lists[i+1]
                else : 
                    list2 = None
                
                merged_lists.append(self.merge2lists(list1, list2))
               
            lists = merged_lists

        return lists[0]

    def merge2lists(self, l1 , l2 ) -> ListNode:
        dummy = ListNode(0)
        curr = dummy

        while (l1 and l2):
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next

        if l1 :
            curr.next = l1
        else:
            curr.next = l2
        
        return dummy.next


                

                

