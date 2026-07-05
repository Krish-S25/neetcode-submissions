class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {

        if(head == nullptr || head->next == nullptr || left == right)
            return head;

        ListNode* curr = head;
        ListNode* prev = nullptr;
        int revLen = right - left + 1;
        
        while(--left){
            prev = curr;
            curr = curr->next;
        }

        ListNode* leftPrev = prev;
        ListNode* reverseStart = curr;

        while(revLen--){

            ListNode* next = curr->next;

            curr->next = prev;

            prev = curr;

            curr = next;
        }

        if(leftPrev)
            leftPrev->next = prev;
        else
            head = prev;

        reverseStart->next = curr;

        return head;
    }
};