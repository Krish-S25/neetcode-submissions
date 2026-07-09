/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
unordered_map<Node* , Node*> old_new;
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node==nullptr){ return nullptr; } 

        if (old_new.count(node)){ return old_new[node]; } //Already existing nodes

        Node* copy = new Node(node->val);  //Make new copy node
        old_new[node] = copy;    //Update old to new hash map

        for(Node* nbr : node-> neighbors){
            copy->neighbors.push_back(cloneGraph(nbr));
        }             //Map the neighbor copies to current node copy
        return copy;
    }  
};
