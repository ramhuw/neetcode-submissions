class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    majorityElement(nums: number[]): number[] {
        let map = new Map<number, number>();
        let ans = [];
        for (const n of nums) {
            map.set(n, (map.get(n) ?? 0) + 1);
        }
        for (const [k, v] of map) {
            if (v > Math.floor(nums.length/3)) {
                ans.push(k);
            }
        }
        return ans;
    }
}
