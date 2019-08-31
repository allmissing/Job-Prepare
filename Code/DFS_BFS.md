# 深度优先搜索与广度优先搜索
###### 深度优先搜索
策略：撞了南墙再回头，递归，在树中是前序遍历

###### 广度优先遍历
策略：影分身同时走，队列+循环，在树中是层次遍历

## 模板
##### 矩阵内dfs模板

    class Solution {
        public void solve(char[][] board) {
            if (board == null || board.length == 0) return;
            int m = board.length;
            int n = board[0].length;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (需要搜索的条件) {
                        dfs(board, i, j);
                    }
                }
            }
        }

        public void dfs(char[][] mat, int i, int j) {
            if (i < 0 || j < 0 || i >= board.length  || j >= board[0].length || 判定条件) {
                // 边界条件（前4个）+判定条件（判定是否还处在同一个连通域）
                return;
            }
            /*这里写遍历时对一个连通域需要的操作*/
            dfs(mat, i - 1, j); // 上
            dfs(mat, i + 1, j); // 下
            dfs(mat, i, j - 1); // 左
            dfs(mat, i, j + 1); // 右
        }
    }


## 实战
###### leetcode 130.被围绕的区域（同是广联达笔试第二题）
思路：从外围0开始搜索，与外围0相连的都应该不变，先用特殊符号标记，然后再遍历整个矩阵，遇见0变为x，遇见特殊符号变回0，搜索部分用dfs/bfs

###### leetcode 200.岛屿数量
思路：遇见1开始dfs，遍历过的1将它变成0，同时dfs过程不计数
