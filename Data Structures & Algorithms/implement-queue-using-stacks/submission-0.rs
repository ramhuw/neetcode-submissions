struct MyQueue {
    queue: Vec<i32>
}

impl MyQueue {
    pub fn new() -> Self {
        Self {
            queue: Vec::new()
        }
    }

    pub fn push(&mut self, x: i32) {
        self.queue.push(x)
    }

    pub fn pop(&mut self) -> i32 {
        let mut new_queue = Vec::new();
        while self.queue.len() > 1 {
            new_queue.push(self.queue.pop().unwrap());
        }
        let ans = self.queue.pop().unwrap();
        self.queue = Vec::new();
        while let Some(a) = new_queue.pop() {
            self.queue.push(a);
        }
        ans
    }

    pub fn peek(&self) -> i32 {
        let mut temp = self.queue.clone();
        while temp.len() > 1 {
            temp.pop().unwrap();
        }
        temp.pop().unwrap()
        
    }

    pub fn empty(&self) -> bool {
        self.queue.is_empty()
    }
}

// Your MyQueue object will be instantiated and called as such:
// let obj = MyQueue::new();
// obj.push(x);
// let ret_2: i32 = obj.pop();
// let ret_3: i32 = obj.peek();
// let ret_4: bool = obj.empty();
