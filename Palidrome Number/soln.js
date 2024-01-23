/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0) {
        return false;
    }
    if (x < 10) {
        return true;
    }
    x = String(x);
    for (let index = 0; index < x.length/2; index++) {
        const first = x[index];
        const second = x[x.length - index - 1];
        if (first !== second) {
            return false;
        }
    }
    return true;
};

console.log(isPalindrome(1001));