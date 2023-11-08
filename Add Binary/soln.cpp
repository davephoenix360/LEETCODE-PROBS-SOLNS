#include<bits/stdc++.h>
using namespace std;

string addBinary(string a, string b) {
    //Make 'a' the larger string
    string ans="";
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int next_a, next_b, res, carry = 1;
    string::iterator it_a = a.begin(), it_b = b.begin();

    while (it_a != a.end() || it_b != b.end())
    {
        if(it_a == a.end()){next_a = 0;}
        else{next_a = *it_a - '0';it_a++;}
        if(it_b == b.end()){next_b = 0;}
        else{next_b = *it_b - '0';it_b++;}

        res = next_a + next_b + carry;
        if(res > 1){carry = 1; res = res % 2;}
        else{carry = 0;}

        ans += '0' + res;  
        cout << ans << endl;
        res = 0; 
    }

    if (carry == 1)
    {
        ans += '1';
    }
    
    reverse(ans.begin(), ans.end());

    return ans;
    
}

int main()
{
    string a = "110", b = "1100";
    cout << addBinary(a, b);

    return 0;

}