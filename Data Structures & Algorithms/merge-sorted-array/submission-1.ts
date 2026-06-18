class Solution {
    /**
     * @param {number[]} nums1
     * @param {number} m
     * @param {number[]} nums2
     * @param {number} n
     * @return {void} Do not return anything, modify nums1 in-place instead.
     */
    merge(nums1: number[], m: number, nums2: number[], n: number): void {
        let i = 0;
        let j = 0;
        while (j < n) {
            while (nums1[i] <= nums2[j] && i < m + j) {
                i += 1;
            }
            let t = nums2[j];
            for (let k = i; k < m + n; k++) {
                let f = nums1[k];
                nums1[k] = t;
                t = f;
            }
            i += 1;
            j += 1;
        }
    }
}
