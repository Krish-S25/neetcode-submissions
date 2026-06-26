class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode* head = l1;
        ListNode* prev = nullptr;

        int carry = 0;   

        while(l1 || l2){
            if(!l1){                //when l1 hits nullptr
                prev->next = l2;
                l1 = l2;
                l2 = nullptr;
            }
            int sum = l1->val + carry;
            if(l2){                //when l2 is not nullptr
                sum += l2->val;    
                l2 = l2->next;    
            }
            carry = sum / 10;      
            l1->val = sum % 10;
            prev = l1;

            l1 = l1->next;      //move next
        }
                                  //Useful when carry!=0 and size(l1) = size(l2)
        if(carry){  prev->next = new ListNode(carry);  } 

        return head;
    }
};