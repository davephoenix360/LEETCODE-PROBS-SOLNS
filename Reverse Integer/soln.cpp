/*
This was the top solution on Leetcode. The intuition is just a simple algorithm with afew edge cases handled.
Edge Cases: Overflow and Underflow
*/


#include<bits/stdc++.h>
using namespace std;

class Solution {                      
public:
    int reverse(int x) {
        long ans = 0;
        while(x){
            int rem = x%10;
            ans = ans*10+rem;
            x=x/10;
        }  

        if(ans>INT_MAX || ans<INT_MIN){
            return 0;
        }
        else{
            return int(ans);
        }
       
         
    }
}; 
int main()
{
    Solution mySoln;
    //cout << mySoln.isOkay(1123456781);
    //cout << mySoln.reverse(-2147483648) << endl;
    int mine = -2147483647;
    cout << mine << endl;
    //cout << 1123456789 << endl;
    //cout << INT32_MAX;
    return 0;
}