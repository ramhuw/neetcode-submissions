use std::ops::{Add, Mul};
impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        let n1 = Natural::new(&num1);
        let n2 = Natural::new(&num2);
        return n1.mul(n2).get_string();
    }
}

fn converter(c: char) -> u8 {
    c as u8 - '0' as u8
}

struct Natural {
    digits: Vec<u8>
}

impl Natural {

    fn new(num: &str) -> Self {
        Self {
            digits: num.chars().map(converter).rev().collect::<Vec<u8>>()
        }
    }

    fn get(&self, i: usize) -> Option<u8> {
        self.digits.get(i).map(|x| *x)
    }

    fn len(&self) -> usize {
        self.digits.len()
    }

    fn get_string(&self) -> String {
        self.digits.iter().rev().map(|d| d.to_string()).collect::<Vec<String>>().join("")
    }
}
impl Add<Natural> for Natural {
    type Output = Natural;
    fn add(self, other: Self) -> Self {
        let mut sum: Vec<u8> = Vec::new();
        let mut carry: u8 = 0;
        for i in 0..self.len().max(other.len()) {
            let x = match self.get(i) {
                Some(x) => x,
                None => 0
            };
            let y = match other.get(i) {
                Some(y) => y,
                None => 0
            };
            sum.push((x + y + carry) % 10);
            carry = (x + y + carry) / 10;
        }
        if carry != 0 {
            sum.push(carry);
        }
        Natural {
            digits: sum
        }
    }
}

impl Mul<Natural> for Natural {
    type Output = Natural;
    fn mul(self, other: Self) -> Self {
        let mut prod = Natural::new("0");
        for i in 0..self.len() {
            for j in 0..other.len() {
                let p = self.digits[i] * other.digits[j];
                if p != 0 {
                    prod = prod.add(Self::new(&(p.to_string() + "0".repeat(i + j).as_str())));
                }
            }
        }
        return prod
    }
}