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
    
    map<int, int> inIndex;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        
        int pl = 0, il = 0;
        int pr = preorder.size() - 1;
        int ir = inorder.size() - 1;
        for(int i =0; i<=ir; i++)
            inIndex[inorder[i]] = i;
        
        return helper(pl, pr, preorder, il, ir, inorder);
        
    }
    
    TreeNode* helper(int p1, int p2, vector<int>& pre, int i1, int i2, vector<int>&in){
        
        if(p1 > p2 || i1 > i2) return NULL;
        int val = pre[p1];
        TreeNode* root = new TreeNode(val);
        
        int in_split = inIndex[val];
        int pre_split = p1 + (in_split - i1);
        
        root->left = helper(p1+1, pre_split, pre, i1, in_split-1, in);
        root->right = helper(pre_split+1, p2, pre, in_split+1, i2, in);
        
        return root;

    }
};
