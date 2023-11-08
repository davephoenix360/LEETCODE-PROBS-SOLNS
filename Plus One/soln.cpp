#include<bits/stdc++.h>
using namespace std;

vector<int> plusOne(vector<int>& digits) {
        vector<int> new_digits;
        int carry = 1, ans;

        for (auto i = digits.end()-1; i >= digits.begin(); i--)
        {
                ans = *i + carry;
                new_digits.insert(new_digits.begin(), ans % 10);
                if(ans > 9){carry = 1;}
                else{carry = 0;}
        }
        if (carry == 1)
        {
                new_digits.insert(new_digits.begin(), carry);
        }
        
        return new_digits;
}

int main()
{
        vector<int> digits = {9};
        auto res = plusOne(digits);
        for (auto i : res)
        {
                cout << " " << i ;
        }
        
        return 0;
}

