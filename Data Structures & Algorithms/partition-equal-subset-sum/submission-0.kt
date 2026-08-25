class Solution {
    fun canPartition(nums: IntArray): Boolean {
        val sum = nums.sum()
        if (sum % 2 == 1) {
            return false
        } else {
            val half = sum / 2;
            val d: BooleanArray = BooleanArray(half + 1) { false }
            d[0] = true
            for (x in nums) {
                for (i in (0..half).reversed()) {
                    if (d[i] && i + x <= half) {
                        d[i+x] = true
                    }
                }
            }
            return d[half]
        }
    }
}