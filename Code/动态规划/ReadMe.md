# 动态规划

## 0-1背包问题（常考）

    public class BagDP {
        public static void main(String[] args) {
            int[] weig = new int[]{4,6,2,8,4,3};
            int[] bene = new int[]{2,5,3,4,7,6};
            int  cons = 10;
            BagDP bdp = new BagDP();
            int res = bdp.bagbp(weig,bene,cons);
            System.out.println(res);
        }
        /*
        * dp问题需要搞清楚的几个点：
        * 1. DP表中存放的是什么
        * 2. 状态转移方程
        * */

        /*
        * 背包问题的逻辑：
        * 1. 背包容量从小往大累计考虑，先计算只有第一件物品，分别装进容量不断增大的背包能带来的最大收益
        *    然后计算有前两件物品，分别装进容量不断增大的背包带来的最大收益
        *    当商品不断增多，超过背包容量时就涉及到舍取问题了
        *    这样，dp表中存放的是由前i件商品，对于容量为j的背包能带来的最大收益
        * 2. 如果当前物品i的重量大于背包空间j,那么该物品不能装，结果和只有i-1个物品是一样的
        *    如果小于，那么取装和不装利益最大：其中装的话，等价于j中i物品大小的空间的大小已经占用，剩余空间j-weighti是一个优化子问题，查表
        * 3. 注意i,j从1开始，weight，bene从0索引，查这两个表时减1
        * */
        public int bagbp(int[] weight, int[] bene, int Constrain){
            int NofThing = weight.length;
            int[][] dp = new int[NofThing+1][Constrain+1];
            for(int i=1;i<=NofThing;i++){
                for(int j=1;j<=Constrain;j++){
                    if(weight[i-1]>j) dp[i][j] = dp[i-1][j];
                    else dp[i][j] = Math.max(dp[i-1][j-weight[i-1]]+bene[i-1], dp[i-1][j]);
                }
            }
            return dp[NofThing][Constrain];
        }
    }
