/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     var val: Int
 *     var left: TreeNode?
 *     var right: TreeNode?
 *     init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */

class Solution {
    func postorderTraversal(_ root: TreeNode?) -> [Int] {
        guard let root = root else {return []}
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    }
}
