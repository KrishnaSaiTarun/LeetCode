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

    
    vector<int> preorderTraversal(TreeNode* root) {
        
        vector<int> ret;
        
        if(root==NULL) return ret;
        
        stack<TreeNode*> s;
        
        s.push(root);
        
        while(!s.empty()){
            
            TreeNode* cur = s.top();
            ret.push_back(cur->val);
            s.pop();
            if(cur->right!=NULL)
            s.push(cur->right);
            if(cur->left!=NULL)
            s.push(cur->left);
        }
        
        return ret;
        
//         if(root==NULL) return ret;
        
//         ret.push_back(root->val);
//         preorderTraversal(root->left);
//         preorderTraversal(root->right);
        
//         return ret;
        
        
    }
};
