# 动态规划

## 0-1背包问题（常考）
特点：用约束来当一个轴

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

## 最大值最小化类动态规划模板
#### 状态转移方程
f[i][j] = min{max{f[i][1]-f[k][1],f[k][j-1]}},其中max：1<=k<=i，在k范围内，两部分取最大最小值  
f[i][j]标识前i个数据分成j段的最大最小值  
f[i][1]-f[k][1]表示k~i的值  
f[k][j-1]表示前k个数据分成j-1段的最大最小值  
#### 代码实现

        static int schedule(int m,int[] array) {
            int min,temp,k;
            int[][] dp = new int[array.length+1][m+1];
            for(int i=1;i<=array.length;i++) dp[i][1] = dp[i-1][1]+array[i-1];
            for(int i=2;i<=array.length;i++){
                for(int j=2;j<=m;j++){
                    for(k=1,temp=Integer.MAX_VALUE;k<i;k++){
                        min = Math.max(dp[i][1]-dp[k][1],dp[k][j-1]);
                        temp = min<temp?min:temp;
                    }
                    dp[i][j] = temp;
                }
            }
            return dp[array.length][m];
        }
