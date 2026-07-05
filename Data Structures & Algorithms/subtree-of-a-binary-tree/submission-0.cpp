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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p == nullptr && q == nullptr){    //Only for BOTH end points
            return true;
        }
        if(p == nullptr || q == nullptr){    //Only one end point since it PASSED AND earlier
            return false;
        }
        if( p->val != q->val ){             // Check same values
            return false;
        }
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    } 
                                      //^^^^^^Classic code reuse of previous QUESTION^^^^^
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(root == nullptr && subRoot != nullptr){ return false; }

        if(isSameTree(root,subRoot)){
            return true;   //Check if current root node is matching subroot 
        }
        
        return (isSubtree( root->left,subRoot)) || (isSubtree(root->right,subRoot));   // NOW Check both children
    }
};
