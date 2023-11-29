#include<bits/stdc++.h>
using namespace std;

int lengthOfLongestSubstring(string s) {
    int count=0, i=0, j;
    map<char, int> subs;
    while (i < s.length())
    {
        subs.clear();

        for(j = i; j < s.length(); j++)
        {
            if(subs[s[j]] != 1)
            {
                subs[s[j]] = 1;
                if (j+1 == s.length())
                {
                    if(j-i+1 > count)
                    {
                        count = j-i+1;
                    }
                }
                
            }
            else
            {
                if(j-i > count)
                {
                    count = j-i;
                }
                break;
            }

        }
        i++;
    }
    
    if(s.length()==1)
    {
        return 1;
    }

    return count;

}

int main()
{
    cout << lengthOfLongestSubstring("a");
    return 0;
}