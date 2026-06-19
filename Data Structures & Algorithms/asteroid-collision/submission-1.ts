class Solution {
    /**
     * @param {number[]} asteroids
     * @return {number[]}
     */
    asteroidCollision(asteroids: number[]): number[] {
        let stack = [];
        for (const b of asteroids) {
            let blive = true;
            while (stack.length > 0) {
                let a = stack.pop();
                if (b < 0 && a > 0) {
                    if (Math.abs(a) > Math.abs(b)) {
                        stack.push(a);
                        blive = false;
                        break;
                    }
                    if (Math.abs(a) === Math.abs(b)) {
                        blive = false
                        break;
                    }
                } else {
                    stack.push(a);
                    break;
                }
            }
            if (blive) {
                stack.push(b);
            }
        }
        return stack;
    }
}
