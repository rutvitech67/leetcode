class Solution {
public:

    TreeNode* findMin(TreeNode* root)
    {
        while(root->left)
        {
            root = root->left;
        }

        return root;
    }

    TreeNode* deleteNode(TreeNode* root, int key)
    {
        if(root == nullptr)
            return nullptr;

        if(key < root->val)
        {
            root->left =
                deleteNode(root->left, key);
        }

        else if(key > root->val)
        {
            root->right =
                deleteNode(root->right, key);
        }

        else
        {
            // No child
            if(root->left == nullptr &&
               root->right == nullptr)
            {
                return nullptr;
            }

            // One child
            if(root->left == nullptr)
            {
                return root->right;
            }

            if(root->right == nullptr)
            {
                return root->left;
            }

            // Two children
            TreeNode* successor =
                findMin(root->right);

            root->val =
                successor->val;

            root->right =
                deleteNode(root->right,
                           successor->val);
        }

        return root;
    }
};