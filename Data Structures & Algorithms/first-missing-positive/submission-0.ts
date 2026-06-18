class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    firstMissingPositive(nums: number[]): number {
        let set = new Set<number>(nums);
        let n = 1;
        while (set.has(n)) {
            n += 1;
        }
        return n;
    }
}
