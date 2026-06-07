class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        var map: HashSet<Int> = hashSetOf()
        for (n in nums) {
            if (!map.contains(n)) {
                map.add(n)
            } else {
                return true
            }
        }
        return false
    }
}
