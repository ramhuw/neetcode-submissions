class Solution {
    fun search(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.size
        while (left + 1 < right) {
            val middle = (left + right) / 2
            if (nums[middle] < nums[0]) {
                right = middle
            } else {
                left = middle
            }
        }
        val start = right.mod(nums.size)
        left = start.mod(nums.size)
        right = (start - 1).mod(nums.size)
        while (left != right) {
            val middle = if (left > right) ((left + right + nums.size) / 2).mod(nums.size)
            else (left + right) / 2
            if (nums[middle] == target) {
                return middle
            } else if (nums[middle] < target) {
                left = (middle + 1).mod(nums.size)
            } else {
                right = (middle).mod(nums.size)
            }
        }
        return if (nums[right] == target) {right} else {-1}
    }
}
