/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        
        stack<TreeNode*> s;
        vector<int> ret;
        if(root == NULL) return ret;
        
        s.push(root);
        
        while(!s.empty()){
            
            root = s.top();
            s.pop();
            
            ret.push_back(root->val);
            
            if(root->left!=NULL)
                s.push(root->left);
            
            if(root->right!=NULL)
                s.push(root->right);  

        }
        
        int l = 0;
        int r = ret.size()-1;
        while(l<r){
            
            
            int temp = ret[l];
            ret[l] = ret[r];
            ret[r] = temp;
            
            l++; r--;
        }
        
        return ret;
        
    }
};
