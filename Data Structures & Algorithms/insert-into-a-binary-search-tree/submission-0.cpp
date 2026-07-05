/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* cur = root;               //Keeps track of the position we insert into
        if(root == nullptr) { return new TreeNode(val); }
        TreeNode* prev = nullptr;           //Keeps track of previous node of cur
        while(cur){
            prev = cur;
            if((cur->val) > val){     //Navigates to the LEFT
                cur = cur->left;
            }
            else{
                cur = cur->right;    //Navigates to the RIGHT
            }
        }
        //Finding the correct slot from PREV
        if(prev->val > val){ prev->left = new TreeNode(val); }

        else{ prev->right = new TreeNode(val); }

        return root;
        
    }
};