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
    
    map<int, int> InorderIndex;
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        
        int lp = postorder.size();
        int li = inorder.size();
        
        for(int i = 0; i< li; i++)
            InorderIndex[inorder[i]] = i;
        
        return helper(0, li-1, inorder, 0, lp-1, postorder);

    }
    
    TreeNode* helper(int in1, int in2, vector<int>& in, int p1, int p2, vector<int>&post){
        
        
        
        if(in1 > in2 || p1>p2) return NULL;
        
        int val = post[p2];
        
        TreeNode* root = new TreeNode(val);
        int i_split = InorderIndex[val];
        int p_split = p1 + (i_split - in1)-1;
        root->left = helper(in1, i_split-1, in, p1, p_split, post);
        root->right = helper(i_split+1, in2, in, p_split+1, p2-1, post );
        
        return root;
        
        
        
        
    }
};
