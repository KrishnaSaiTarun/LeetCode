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
    vector<int> inorderTraversal(TreeNode* root) {
        
        vector<int> ret;
        
        if(root==NULL) return ret;
        
        stack<TreeNode*> s;
        
        
        while(1){
            
            while(root){
                s.push(root);
                root = root->left;
            }
            if(s.empty()) break;
            
            root = s.top();
            s.pop();
            ret.push_back(root->val);
            root = root->right;
            

        }
        
        return ret;
        
    }
};
