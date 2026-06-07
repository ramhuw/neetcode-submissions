class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        var map: HashMap<Int, Int> = hashMapOf()
        for (n in nums) {
            if (!map.containsKey(n)) {
                map[n] = 0
            } else {
                return true
            }
        }
        return false
    }
}
