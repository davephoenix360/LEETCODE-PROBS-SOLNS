// Leetcode Problem

#include<bits/stdc++.h>
using namespace std;

int getLength(int num)
{
    int len = 0;
    while(num > 0)
    {
        num = num / 10;
        len++;
    }
    return len;
}

string intToRoman(int num) {
    string roman = "";
    string lFives[4] = {"I", "X", "C", "M"};
    string mFives[3] = {"V", "L", "D"};
    int first;
    while(num > 0)
    {
        int len = getLength(num);
        int power = pow(10, len-1);
        first = num/power;
        while(first > 0)
        {
            if(first == 9) {roman = roman + lFives[len-1] + lFives[len]; first -= 9;}
            else if(first >= 5) {roman = roman + mFives[len-1]; first -= 5;}
            else if(first == 4) {roman = roman + lFives[len-1] + mFives[len-1]; first -= 4;}
            else {roman = roman + lFives[len-1]; first--;}
        }
        num = num % power;
        len--;
    }
    return roman;
}

int main()
{
    int num;
    cout << "Enter number you want to change: " << endl;
    cin >> num;
    cout << intToRoman(num);
    return 0;
}