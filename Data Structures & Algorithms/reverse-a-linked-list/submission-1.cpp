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
 #include <vector>

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* pt1 = head;
        ListNode* pt2 = nullptr;
        while(pt1){
            ListNode* temp = pt1->next;
            pt1->next = pt2;
            pt2 = pt1;
            pt1= temp;
        }
        return pt2;
    }
};
