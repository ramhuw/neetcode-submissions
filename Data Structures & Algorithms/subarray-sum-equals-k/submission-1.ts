class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraySum(nums: number[], k: number): number {
        let c = 0;
        let s = [0];
        for (const n of nums) {
            c += n;
            s.push(c);
        }
        let ans = 0;
        for (let i = 0; i <= nums.length; i++) {
            for (let j = i + 1; j <= nums.length; j++) {
                if (s[j] - s[i] === k) {
                    ans += 1;
                }
            }
        }
        return ans;
    }
}
