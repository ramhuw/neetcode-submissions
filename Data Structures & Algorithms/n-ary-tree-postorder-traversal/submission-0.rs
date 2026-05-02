// Definition for a N-ary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct Node {
//     pub val: i32,
//     pub children: Vec<Rc<RefCell<Node>>>,
// }
//
// impl Node {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         Node {
//             val,
//             children: Vec::new(),
//         }
//     }
// }

use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn postorder(root: Option<Rc<RefCell<Node>>>) -> Vec<i32> {
        match root {
            None => Vec::new(),
            Some(r) => {
                let mut ans = Vec::new();
                for child in r.borrow().children.clone() {
                    ans.extend_from_slice(&Solution::postorder(Some(child.clone())))
                }
                ans.push(r.borrow().val);
                ans
            }
        }
    }
}
