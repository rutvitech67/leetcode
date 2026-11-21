class Solution {
public:

    vector<TreeNode*> nodes;

    void preorder(TreeNode* root)
    {
        if(root == nullptr)
            return;

        nodes.push_back(root);

        preorder(root->left);
        preorder(root->right);
    }

    void flatten(TreeNode* root) {
        if(root == nullptr)
        return;
        preorder(root);
        for(int i = 0; i + 1 < nodes.size(); i++){
        nodes[i]->left = nullptr;
        nodes[i]->right = nodes[i + 1];
         }

        nodes.back()->left = nullptr;
        nodes.back()->right = nullptr;
}
};