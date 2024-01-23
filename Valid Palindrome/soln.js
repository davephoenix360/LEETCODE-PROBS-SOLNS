/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.toLowerCase().trim();
    var summation = s.length - 1;
    var f_ptr = 0;
    var s_ptr = summation - f_ptr;
    var myCheck = false;
    while (f_ptr < s_ptr) {
        var first = s[f_ptr];
        var second = s[s_ptr];
        if ((first < 'a' || first > 'z') && (first < '0' || first > '9')) {
            f_ptr++;
            summation++;
        }
        else if((second < 'a' || second > 'z') && (second < '0' || second > '9')) {
            s_ptr--;
            summation--;
        }
        else if (first !== second) {
            return false;
        }
        else{
            f_ptr++;
            s_ptr--;
        }
    }
    return true;

};


console.log(isPalindrome("0P"));
//console.log('a' <= 'g' && 'g' <= 'z');
