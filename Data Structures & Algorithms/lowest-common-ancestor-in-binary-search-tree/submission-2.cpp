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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        while(root!= nullptr){
            if( root->val < p->val && root->val < q->val ){       //When p and q to RIGHT sub-tree
                        root = root->right;    //Optimal soln. from hints           
            }                                  //Can be done with recursion
            else if( root->val > p->val && root->val > q->val ){  //When p and q to LEFT sub-tree
                root = root->left;
            }
            else{
                return root;  //When p and q are both on DIFFERENT sub-tree sides
            }
        }
        return nullptr;
    }
};
