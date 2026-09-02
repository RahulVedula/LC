class Solution {
public:
    int reverse(int x) {
        string newString = "";
        string s = to_string(x);
        for (int i = s.length()-1;i >= 0;i--){
            newString += s[i];
        }
        long int num = stol(newString);
        if (num < pow(-2,31) || num > pow(2,31)-1){
            return 0;
        }
        else if (x < 0){
            num = num - 2*num;
        }
        return num;
    }
};