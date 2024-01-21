/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var characters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000};
    var result = 0;
    
    for (let index = 0; index < s.length; index++) {
        const character = s[index];
        if (index < s.length - 1) {
            if (characters[character] < characters[s[index+1]]) {
                result += characters[s[index+1]] - characters[character]; 
                index++;
            }
            else{
                result += characters[character];
            }
        }
        else{
            result += characters[character];
        }
    }
    return result;
};

console.log(romanToInt("MCMXCIV"))