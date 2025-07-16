class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // Base cases
        if (p == null && q == null) return true;     // Both are null
        if (p == null || q == null) return false;    // One is null
        if (p.val != q.val) return false;            // Values don't match

        // Recursive check
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
