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
    bool isSymmetric(TreeNode* root) {
        
        if(root == NULL) return true;
        
        return isMirror(root->left, root->right);
    
    }
    
    bool isMirror(TreeNode* l_tree, TreeNode* r_tree){
        
        if(l_tree == NULL && r_tree == NULL) return true;
        if(l_tree == NULL || r_tree == NULL) return false;
        
    
        return (l_tree->val == r_tree->val && isMirror(l_tree->left, r_tree->right) && isMirror(l_tree->right, r_tree->left));
        
    }
    
    
};
