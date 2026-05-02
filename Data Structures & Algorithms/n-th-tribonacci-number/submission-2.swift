class Solution {
    func tribonacci(_ n: Int) -> Int {
        var stack = [0, 1, 1]
        if n >= 3 {
            for i in 3...n {
                stack.append(stack[i-1] + stack[i-2] + stack[i-3])
            }   
        }
        return stack[n]
    }
}
