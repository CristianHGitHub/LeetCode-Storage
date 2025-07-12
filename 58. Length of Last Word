class Solution {
public:
    int lengthOfLastWord(string s) {
        int count = 0;
        int last = 0;
        for (auto c: s){
            if (c == ' ') {
                count = 0;
            }
            else {
                count++;
                last = count;
            }
        }
        return last;
    }
};
