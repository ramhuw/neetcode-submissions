class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        var map = mutableMapOf<Int, Int>()
        for (i in 0 until nums.count()) {
            if (map.containsKey(target - nums[i])) {
                return intArrayOf(map[target - nums[i]]!!, i)
            } else {
                map.put(nums[i], i)
            }
        }
        return intArrayOf()
    }
}
