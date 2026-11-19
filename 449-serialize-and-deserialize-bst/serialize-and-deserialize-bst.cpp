class Codec {
public:
    int idx = 0;
    void preorder(TreeNode* root, string& s)
    {
        if(root == nullptr)
            return;
        s += to_string(root->val) + ",";
        preorder(root->left, s);
        preorder(root->right, s);
    }

    string serialize(TreeNode* root)
    {
        string s;
        preorder(root, s);
        return s;
    }

    TreeNode* build(vector<int>& pre, int bound)
    {
        if(idx == pre.size() || pre[idx] > bound)
            return nullptr;
        TreeNode* root = new TreeNode(pre[idx++]);
        root->left = build(pre, root->val);
        root->right = build(pre, bound);
        return root;
    }

    TreeNode* deserialize(string data)
    {
        if(data.empty())
            return nullptr;

        vector<int> pre;

        stringstream ss(data);
        string token;

        while(getline(ss, token, ','))
        {
            if(!token.empty())
                pre.push_back(stoi(token));
        }

        idx = 0;

        return build(pre, INT_MAX);
    }
};