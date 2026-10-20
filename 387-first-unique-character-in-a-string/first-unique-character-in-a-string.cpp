class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> banana;
        for (char ch : s) {
            banana[ch]++;
        }
        for (int i = 0; i < s.size(); i++) {
            if (banana[s[i]] == 1) {
                return i;
            }
        }

        return -1;
    }
};