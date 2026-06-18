class Solution {
    /**
     * @param {string} word1
     * @param {string} word2
     * @return {string}
     */
    mergeAlternately(word1: string, word2: string): string {
        let i = 0;
        let j = 0;
        let w1 = [...word1];
        let w2 = [...word2];
        let ans = '';
        while (i < w1.length || j < w2.length) {
            if (i < w1.length) {
                ans += w1[i];
                i += 1;
            }
            if (j < w2.length) {
                ans += w2[j];
                j += 1
            }
        }
        return ans;
    }
}
