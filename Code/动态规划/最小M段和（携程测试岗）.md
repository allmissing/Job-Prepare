# 携程测试开发笔试题第2题：最小M段和

## 题目描述（非原描述，原描述改变为大数据节点分配问题）
给定n个整数组成的序列，现在要求将序列分割成m段，每段子序列中的数在原序列中连续排列，如何分割才能使这m段子序列的和的最大值达到最小

#### 测试用例
输入：  
> 3 5  
> 1 5 3 4 2  
输出：6  

## 解法1：递归分治（超时，45%）

    import java.util.*;
    public class Minimize_M_sum {
        public static int mint = Integer.MAX_VALUE;

        ******************************开始写代码******************************/
        static void schedule(int m,int[] array,int pin, int maxv) {
            if(m<0) return;
            if(m==0 && pin == array.length)
                if(maxv<mint){
                    mint=maxv;
                    return;
                }
            int count=0;
            for(int i=pin;i<array.length;i++){
                count+=array[i];
                schedule(m-1,array,i+1,Math.max(maxv,count));
                if(array.length-i-1<m) break;
            }
        }
        /******************************结束写代码******************************/

        public static void main(String[] args){
            Scanner in = new Scanner(System.in);
            int m = in.nextInt();
            int size  = in.nextInt();
            int[] array = new int[size];
            for(int i = 0; i < size; i++) {
                array[i] = in.nextInt();
            }
            schedule(m,array,0,0);
            System.out.println(String.valueOf(mint));
        }
    }
    
## 解法2：动态规划（线下编的，线上不知道能不能过）

    import java.util.*;
    /*思路
    * f[i][j] = min{max{f[i][1]-f[k][1],f[k][j-1]}},其中max：1<=k<=i，在k范围内，两部分取最大最小值
    * f[i][j]标识前i个数据分成j段的最大最小值
    * f[i][1]-f[k][1]表示k~i的值
    * f[k][j-1]表示前k个数据分成j-1段的最大最小值
    * */
    public class Minimize_M_sum2 {

        /*******************************开始写代码******************************/
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
        /******************************结束写代码******************************/

        public static void main(String[] args){
            Scanner in = new Scanner(System.in);
            int m = in.nextInt();
            int size  = in.nextInt();
            int[] array = new int[size];
            for(int i = 0; i < size; i++) {
                array[i] = in.nextInt();
            }
            int res = schedule(m,array);
            System.out.println(String.valueOf(res));
        }
    }
