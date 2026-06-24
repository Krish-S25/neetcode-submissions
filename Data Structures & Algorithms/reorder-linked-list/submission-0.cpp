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
    void reorderList(ListNode* head) {
        ListNode* tail = head;
        ListNode* mid = head;
        //----FIND MID POINT AND TAIL------
        while(tail->next && tail->next->next){
            mid = mid->next;  //jumps by 1
            tail = tail->next->next;  //jumps by 2
        }
        //----REVERSE 2nd HALF------
        ListNode* sec = mid->next;
        mid->next = nullptr;      //First iteration
        ListNode* prev = nullptr;
        while(sec){
            ListNode* nxt = sec->next;   
            sec->next = prev;   //Link Reversal part  -> to <-
            prev = sec;         

            sec = nxt ;  //Moves forward ,same as temp = temp->next
        }
        sec = prev;      //Basically original tail or 2ND HALF HEAD
        //----ALTERNATIVELY MERGE first + reversed 2nd half------
        ListNode* fir = head;
        while(sec){
            ListNode* p1 = fir->next ;   //p1 = B 
            ListNode* p2 = sec->next ;   //p2 = C
                                            //Assume [ ..A , B ..... C , D ..]
            fir->next = sec;   //Links A -> D
            sec->next = p1;   //Links D -> B       

            fir = p1;   //Moves A to B
            sec = p2;   //Moves D to C 
        }
        
    }
};
