class Solution {
    func calPoints(_ operations: [String]) -> Int {
        var stack: [Int] = []
        for operation in operations {
            switch operation {
                case "+":
                    stack.append(stack[stack.count - 2] + stack[stack.count - 1])
                case "D":
                    stack.append(stack[stack.count - 1] * 2)
                case "C":
                    stack.remove(at: stack.count - 1)
                default:
                    stack.append(Int(operation)!)
            }
        }
        return stack.reduce(0) { $0 + $1 }
    }
}
