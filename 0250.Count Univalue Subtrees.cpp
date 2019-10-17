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
    int count = 0;
    
    bool is_uni(TreeNode* node) {

      
        if (node->left == NULL && node->right == NULL) {
            count++;
            return true;   
        }

        bool is_unival = true;


        if (node->left != NULL) {
            is_unival = is_uni(node->left) && is_unival && node->left->val == node->val;
         }

        if (node->right != NULL) {
            is_unival = is_uni(node->right) && is_unival && node->right->val == node->val;
        }

        if (!is_unival) return false;
        count++;
        return true;
    }
    
    int countUnivalSubtrees(TreeNode* root) {
        
        if (root == NULL) return 0;
        is_uni(root);
        return count;
        
    }
};
