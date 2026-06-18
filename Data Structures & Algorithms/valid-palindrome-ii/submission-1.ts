class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    validPalindrome(s: string): boolean {
        let chance = true;
        let chars = [...s.toLowerCase()].filter(isAlnum);
        let searches = [[0, chars.length - 1]];
        while (searches.length > 0) {
            let [i, j] = searches.pop();
            if (i >= j) {
                return true;
            }
            if (s[i] === s[j]) {
                searches.push([i + 1, j - 1]);
            } else {
                if (chance) {
                    searches.push([i + 1, j]);
                    searches.push([i, j - 1]);
                    chance = false;
                }
            }
        }
        return false;
    }
    
}
function isAlnum(ch: string): boolean {

  return /^[a-z0-9]$/i.test(ch);

}