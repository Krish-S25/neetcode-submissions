/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head==nullptr){return nullptr;}    //Assume A->B then A'->B'
        unordered_map<Node*, Node*> stores;   //For random take A'->XYZ'
        Node* temp = head;
        while(temp){         //Making copes and storing them in a HASH MAP
            Node* copynode = new Node(temp->val);  
            stores[temp] = copynode;         //put stores[A] = A'
            temp= temp->next;
        }
        temp = head;
        while(temp){          //Make connections between A'
            stores[temp]->next = stores[temp->next];       // A'-> B'
            stores[temp]->random = stores[temp->random];   // A'-> XYZ'
            temp= temp->next;
        }
        return stores[head];
        
    }
};
