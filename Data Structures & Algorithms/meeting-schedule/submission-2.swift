/**
 * Definition of Interval:
 * class Interval {
 *     var start: Int
 *     var end: Int
 *     init(_ start: Int, _ end: Int) {
 *         self.start = start
 *         self.end = end
 *     }
 * }
 */

class Solution {
    func canAttendMeetings(_ intervals: [Interval]) -> Bool {
        let s = intervals.sorted {
            $0.start < $1.start
        }
        let n = s.count
        if n <= 0 {
            return true
        }
        for i in 1..<n {
            if s[i].start < s[i-1].end {
                return false
            }
        }
        return true
    }
}
