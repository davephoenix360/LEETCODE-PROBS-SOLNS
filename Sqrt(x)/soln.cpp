#include<bits/stdc++.h>
using namespace std;

int mySqrt(int x) {
    long long low = 0, high = (x+1)/2, mid;

    while(high - low > 1)
    {
        mid = (low+high)/2;
        if(mid * mid == x)
        {
            return mid;
        }
        else if(mid * mid < x)
        {
            low = mid;
        }
        else
        {
            high = mid;
        }
    }
    if(low * low == x || high*high > x){return low;}
    else
    {
        return high;
    }
    
}

int main()
{
    cout << mySqrt(2147483647);

    return 0;
}