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
        if (p && !q || q && !p) return false;
        if (!p && !q) return true;
        // bfs in both trees and continuously checking for difference 
        // if diff found return false otherwise keep traversing until both ends
        stack<TreeNode*> T1;
        stack<TreeNode*> T2;
        
        T1.push(p);
        T2.push(q);

        while(!T1.empty() && !T2.empty()) {
            TreeNode *n1 = T1.top();
            TreeNode *n2 = T2.top();
            if (n1->val != n2->val)   return false;
            T1.pop(); T2.pop();
            if (n1->right && n2->right) {
                T1.push(n1->right);
                T2.push(n2->right);
            }
            else if (n1->right != n2->right) return false;
            if (n1->left && n2->left) {
                T1.push(n1->left);
                T2.push(n2->left);
            }
            else if (n1->left != n2->left) return false;
        }
        return true;
    }
};
