class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums: number[]): number[] {
        let result = []
        for (let i = 0; i < 2; i++) {
            for (const n of nums) {
            result.push(n)
        }
        }
        return result
    }
}
