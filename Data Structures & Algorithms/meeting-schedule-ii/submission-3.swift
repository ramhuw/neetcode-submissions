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
    func minMeetingRooms(_ intervals: [Interval]) -> Int {
        let intervals = intervals.sorted(by: {$0.start <= $1.start})
        let n = intervals.count
        var rooms: Array<Int> = []
        for interval in intervals {
            if rooms.count == 0 || rooms[0] > interval.start {
                rooms.append(interval.end)
            } else {
                rooms[0] = interval.end
            }
            rooms.sort()
        }
        return rooms.count
    }
}
