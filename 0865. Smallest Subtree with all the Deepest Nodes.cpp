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
    
    TreeNode* lca(TreeNode* root, TreeNode* leftmost, TreeNode* rightmost){
        
        if(!root || root == leftmost || root == rightmost) return root;
        
        TreeNode* left = lca(root->left, leftmost, rightmost);
        TreeNode* right = lca(root->right, leftmost, rightmost);
        
        if(left == NULL) return right;
        if(right == NULL) return left;
        
        return root;
    }
    
    
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        
        if(!root) return root;
        queue<TreeNode*> bfs;
        bfs.push(root);
        TreeNode* leftmost = NULL; 
        TreeNode* rightmost = NULL;
        
        
        while(!bfs.empty()){
            
            int nodesInLevel = bfs.size();
            
            for(int i = 0; i < nodesInLevel; i++){

                TreeNode* node = bfs.front();
                bfs.pop();
                
                if(i == 0) leftmost = node;
                if(i == nodesInLevel - 1) rightmost = node;
                

                
                if(node->left) bfs.push(node->left);
                if(node->right) bfs.push(node->right);               
                
            }
        }
        
        return lca(root, leftmost, rightmost);
        
    }
};
