use std::collections::VecDeque;

struct MyStack {
    stack: VecDeque<i32>
}

impl MyStack {
    pub fn new() -> Self {
        MyStack {
            stack: VecDeque::new()
        }
    }

    pub fn push(&mut self, x: i32) {
        self.stack.push_back(x);
    }

    pub fn pop(&mut self) -> i32 {
        let mut new_stack = VecDeque::new();
        while self.stack.len() > 1 {
            let a = self.stack.pop_front().unwrap();
            new_stack.push_back(a);
        }
        let ans = self.stack.pop_front().unwrap();
        self.stack = new_stack;
        ans
    }

    pub fn top(&self) -> i32 {
        let mut temp = self.stack.clone();
        let mut ans: i32 = 0;
        while let Some(a) = temp.pop_front() {
            ans = a;
        }
        ans
    }

    pub fn empty(&self) -> bool {
        self.stack.is_empty()
    }
}
