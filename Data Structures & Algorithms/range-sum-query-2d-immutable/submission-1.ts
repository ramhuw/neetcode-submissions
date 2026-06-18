class NumMatrix {
    /**
     * @param {number[][]} matrix
     */
    sum: number[][];
    constructor(matrix: number[][]) {
        let m = matrix.length;
        let n = matrix[0].length;
        this.sum = Array.from({ length: m }, () => Array.from({ length: n }, () => 0));
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                this.sum[i][j] = matrix[i][j];
                if (i > 0) {
                    this.sum[i][j] += this.sum[i-1][j];
                }
                if (j > 0) {
                    this.sum[i][j] += this.sum[i][j-1];
                }
                if (i > 0 && j > 0) {
                    this.sum[i][j] -= this.sum[i-1][j-1];
                }
            }
        }
    }

    /**
     * @param {number} row1
     * @param {number} col1
     * @param {number} row2
     * @param {number} col2
     * @return {number}
     */
    sumRegion(row1: number, col1: number, row2: number, col2: number): number {
        let ans = this.sum[row2][col2];
        if (row1 > 0) {
            ans -= this.sum[row1-1][col2];
        }
        if (col1 > 0) {
            ans -= this.sum[row2][col1-1];
        }
        if (col1 > 0 && row1 > 0) {
            ans += this.sum[row1-1][col1-1];
        }
        return ans;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
