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
    vector<vector<int>> levelOrder(TreeNode* root) { //bfs
        vector<vector<int>> R;
        if (!root) return R;
        queue<TreeNode*> nq;
        queue<int> dq;
        nq.push(root);  dq.push(0);
        while(!nq.empty()) {
            int size = nq.size();
            vector<int> V;
            for (int i = 0; i < size; i++){
                TreeNode* N = nq.front(); nq.pop();
                V.push_back(N->val);
                if (N->left)
                    nq.push(N->left);
                if (N->right)
                    nq.push(N->right);
            }
            R.push_back(V);
        }
        return R;
    }
};
