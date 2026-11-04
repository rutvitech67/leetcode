class Solution {
public:
    int distributeCandies(vector<int>& candyType)
    {
        unordered_set<int> s;

        for(int num : candyType)
        {
            s.insert(num);
        }

        int distinct = s.size();

        int allowed =
            candyType.size()/2;

        return min(distinct,
                   allowed);
    }
};