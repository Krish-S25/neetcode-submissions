/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:

    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* fast = head;
        for(int i = 0 ; i < n; i++){    
            fast = fast->next;   //Bring FAST to (head + n) index
        }
        if (!fast) return head->next; //For length = 1 case

        ListNode* slow = head;  //Start SLOW at (head) index 

        while(fast->next){  // Maintain N distance between SLOW and FAST
            fast = fast->next;   
            slow = slow->next;   //Move forwards with both until FAST reaches END
        }
        slow->next = slow->next->next;  //Skip the Nth index node
        return head;
        
    }
};
