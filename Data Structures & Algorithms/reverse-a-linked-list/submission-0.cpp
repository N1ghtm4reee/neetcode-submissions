/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* tmp = nullptr;
        ListNode* n = nullptr;
        ListNode* p = nullptr;
        ListNode* c = head;

        while(c){
            tmp = c->next;
            c->next = p;
            p = c;
            c = tmp;
        }
        return p;
    }
};
