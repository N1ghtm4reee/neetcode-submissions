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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* p = head;
        ListNode* prev = nullptr;
        int len = 0;
        while(p)
        {
            p = p->next;
            len++;
        }
        if (n == len) return head->next;
        p = head;
        int i = 0;
        while(p){
            
            if (i == (len - n))
            {
                prev->next = p->next;
                break;
            }
            prev = p;
            p = p->next;
            i++;
        }
        return head;
    }
};
