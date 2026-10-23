class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        unordered_set<int> a;
        for(int num : nums)
        {  a.insert(num);  }
        vector<int>b;
        for(int i = 1; i <= nums.size(); i++)
        {
            if(a.count(i) == 0)
            {
                b.push_back(i);
            }
        }

        return b;
    }
};