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
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        int maxDepth = 0;
        stack<TreeNode*> node;
        stack<int> depth;
        node.push(root);
        depth.push(1);
        while(!node.empty()) {
            TreeNode* N = node.top(); node.pop();
            int currentDepth = depth.top(); depth.pop();
            maxDepth = max(currentDepth, maxDepth);
            if (N->right)
            {
                node.push(N->right);
                depth.push(currentDepth + 1);
            }
            if (N->left){
                node.push(N->left);
                depth.push(currentDepth + 1);
            }
        }
        return maxDepth;
    }
};
