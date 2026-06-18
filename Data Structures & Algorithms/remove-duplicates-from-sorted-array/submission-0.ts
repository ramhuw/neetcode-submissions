class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums: number[]): number {
        let n = nums.length;
        let i = 0;
        while (i < n - 1) {
            if (nums[i] === nums[i+1]) {
                nums.splice(i, 1);
                n -= 1;
            } else {
                i += 1;
            }
        }
        return n;
    }
}
