class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr) return false;

        // Check if it's a leaf node
        if (root->left == nullptr && root->right == nullptr) {
            return root->val == targetSum;
        }

        // Recur on left and right subtrees
        int newTarget = targetSum - root->val;
        return hasPathSum(root->left, newTarget) || hasPathSum(root->right, newTarget);
    }
};
