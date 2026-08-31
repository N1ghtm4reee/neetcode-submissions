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
    int goodNodes(TreeNode* root) { //dfs
        if (!root) return 0;
        int lastVal = root->val;
        int r = 0;
        stack<TreeNode*> sn; sn.push(root);
        stack<int> sv; sv.push(root->val);

        while(!sn.empty()) {
            TreeNode* N = sn.top(); sn.pop();
            int maxSoFar = sv.top(); sv.pop();

            if (N->left){
                sn.push(N->left);
                sv.push(max(N->left->val, maxSoFar));
            }
            if (N->right){
                sn.push(N->right);
                sv.push(max(N->right->val, maxSoFar));
            }
            if (N->val >= maxSoFar) r++;
            
        }
        return r;
    }
};
