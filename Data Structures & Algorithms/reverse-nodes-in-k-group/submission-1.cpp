class Solution {

public:
    ListNode* reverseSegment(ListNode* head, ListNode* stop) {
        ListNode* prev = stop; // Link tail directly to the next group
        ListNode* curr = head;
        while (curr != stop) {
            ListNode* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }
        return prev;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode dummy(0, head);
        ListNode* groupPrev = &dummy;
        
        while (true) {
            ListNode* kth = groupPrev->next;
            int count = 0;
            
            while (kth != nullptr && count < k) {
                kth = kth->next;   // Scout ahead k steps
                count++;
            }
            
            if (count < k) break;   // If fewer than k nodes remain, leave them as they are
            // Reverse current segment and link it to the previous group
            ListNode* groupStart = groupPrev->next;
            groupPrev->next = reverseSegment(groupStart, kth);

            groupPrev = groupStart;  // Move pointer to the tail of the newly reversed group
        }
        
        return dummy.next;
    }
};