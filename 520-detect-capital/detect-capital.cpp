class Solution {
public:
    bool detectCapitalUse(string word) {

        bool u = true;
        bool l = true;
        for(char ch : word)
        {
            if(!isupper(ch))
                u = false;
            if(!islower(ch))
                l = false;
        }
        if(u || l)
            return true;
        if(isupper(word[0]))
        {
            for(int i = 1; i < word.size(); i++)
            {
                if(!islower(word[i]))
                    return false;
            }
            return true;
        }
        return false;
    }
};