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
    vector<int> rightSideView(TreeNode* root) { // bfs
        if (!root) return vector<int>(0);
        queue<TreeNode*> qn; qn.push(root);
        vector<int> R;
        while(!qn.empty()) {
            int size = qn.size();
            for (int i = 0; i < size; i++){
                TreeNode* N = qn.front(); qn.pop();
                if (N->left) qn.push(N->left);
                if (N->right) qn.push(N->right);
                if (i == size - 1)
                    R.push_back(N->val);
            }
        }
        return R;
    }
};
