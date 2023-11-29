#include<bits/stdc++.h>

using namespace std;

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

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* deleteDuplicates(ListNode* head) {

    if(head != nullptr && head->next != nullptr)
    {
        int myval = head->val;
        int mynextval = head->next->val;

        if(myval == mynextval)
        {
            head->next = head->next->next;
            deleteDuplicates(head);
        }
        else
        {
            deleteDuplicates(head->next);
        }

    }
    else
    {
        return head;
    }
    
    return head;
}

int main()
{
    ListNode i5(4);
    ListNode i4(3, &i5);
    ListNode i3(3, &i4);
    ListNode i2(2, &i3);
    ListNode i1(2, &i2);
    ListNode i0(1, &i1);

    auto head = deleteDuplicates(&i0);

    while (head != nullptr)
    {
        cout << head->val << " ";
        head = head->next;
    }
    
    return 0;
}


