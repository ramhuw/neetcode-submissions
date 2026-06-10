class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let map = new Map<number, number>
        for (const n of nums) {
            if (map.has(n)) {
                return true
            } else {
                map.set(n, 1)
            }
        }
        return false
    }
}
