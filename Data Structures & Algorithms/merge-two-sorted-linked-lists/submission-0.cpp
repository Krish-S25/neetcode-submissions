/**
 * Definition for singly-linked list.
 * struct ListNode {
 *    int val;
 *    ListNode *next;
 *    ListNode() : val(0), next(nullptr) {}
 *    ListNode(int x) : val(x), next(nullptr) {}
 *    ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        //ListNode newList = new ListNode();
        ListNode* newpt = new ListNode();
        ListNode* root = newpt;
        while(list1 && list2){
            if(list1->val > list2->val){
                    newpt->next = list2;
                    list2 = list2->next;
                }
            else if(list1->val <= list2->val){
                    newpt->next = list1;
                    list1 = list1->next;
                }  
            newpt = newpt->next;              
            }
        if (list1) newpt->next = list1;
        if (list2) newpt->next = list2;
        
        return root->next;}
        
};
