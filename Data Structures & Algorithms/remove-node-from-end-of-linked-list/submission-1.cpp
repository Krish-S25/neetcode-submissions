class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        ListNode* tail = head;
        int nodes = 1;

        while(tail->next){
            tail = tail->next;
            nodes++;          //get to TAIL and check the total number of nodes
        }

        if(nodes == 1 && n == 1){
            return nullptr;
        }

        int position = nodes - n + 1;

        if(position == 1){
            return head->next;
        }

        ListNode* targ_1 = head;

        while(position > 2){
            targ_1 = targ_1->next;   //Gets to TARGET - 1
            position -= 1;
        }

        ListNode* targ = targ_1->next;     //Gets to TARGET

        targ_1->next = targ->next;  // Connects TARGET - 1 to TARGET + 1

        return head;
    }
};