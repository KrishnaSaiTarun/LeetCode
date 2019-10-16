/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        int k = lists.size();
        if(k==0) return {};
        if(k==1) return lists[0];
        
        return mergeK(lists, 0, k-1);

        
    }
    
    private:
    
    ListNode* mergeK(vector<ListNode*>& lists, int l, int r){
        
        if(l == r) return lists[l];        
        int m = (l+r)/2;
        
        return merge_two(mergeK(lists, l, m), mergeK(lists, m+1, r));
     
    }
    
    ListNode* merge_two(ListNode* l1, ListNode* l2){
        
        ListNode* ret = new ListNode(0);
        ListNode* list = ret;
            
        
        while(l1!=NULL && l2!= NULL){
            
            if(l1->val<l2->val){
                
                list->next = l1;
                l1 = l1->next;
                
            }
            
            else{
                
                list->next = l2;
                l2 = l2->next;
            }
            
            list = list->next;
        }
        
        if(l1==NULL)
            list->next = l2;
        else
            list->next = l1;
        
        return ret->next;
    }
    

};
