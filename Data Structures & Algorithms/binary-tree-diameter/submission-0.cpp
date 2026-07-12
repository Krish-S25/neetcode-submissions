class Solution {
private:
    int maxDiameter = 0;

    // Helper function that calculates the height of the tree 
    // while updating the maximum diameter found so far.
    int calculateHeight(TreeNode* node) {
        if (node == nullptr) return 0;

        // Recursively find the height of left and right subtrees
        int leftHeight = calculateHeight(node->left);
        int rightHeight = calculateHeight(node->right);

        // The diameter passing through the current node is leftHeight + rightHeight
        maxDiameter = max(maxDiameter, leftHeight + rightHeight);

        // Return the height of the current node up to its parent
        return 1 + max(leftHeight, rightHeight);
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        maxDiameter = 0; // Reset for safety across multiple execution calls
        calculateHeight(root);
        return maxDiameter;
    }
};