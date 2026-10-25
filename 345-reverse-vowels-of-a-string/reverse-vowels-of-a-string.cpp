class Solution {
public:
    string reverseVowels(string s) {
        string vowels = "aeiouAEIOU";
        int left = 0;
        int right = s.size() - 1;
        while (left < right) {
            if (vowels.find(s[left]) == string::npos) {
                left++;
                continue;
            }
            if (vowels.find(s[right]) == string::npos) {
                right--;
                continue;
            }
            swap(s[left], s[right]);
            left++;
            right--;
        }

        return s;
    }
};