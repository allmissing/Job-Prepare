## 基础运算
1. 不使用Math.sqrt方法实现求平方根：https://blog.csdn.net/qq_17776287/article/details/53762265  
   牛顿迭代法快速寻找平方根：假如求a的平方根的近似值，首先随便猜一个近似值x，然后不断令x等于x和a/x的平均数，迭代个六七次x的值就相当准确了。  
   其原理：求平方根等价于求方程x^2-a=0的正实根，f(x)=x^2-a的导数为f'(x)=2x，将f(x)进行一阶泰勒展开得f(x2) = f(x1)+f'(x1)(x2-x1)，将上面的式子代入得到x2 = (x1^2+a)/2*x1  

# 基础临阵磨枪系列

## 快排

    /*快排思路：
    * 通过一趟排序将待排记录分割成独立的两部分，然后递归分别排序两部分
    * */

    public class QuikSort {
        public static void main(String[] args) {
            int[] a = new int[]{2,7,8,4,6,3,9,18,43,22,5,1};
            QuikSort qs = new QuikSort();
            qs.QS(a);
            for(int i=0;i<a.length;i++)
                System.out.print(a[i]+" ");
        }

        public void QS(int[] nums){
            Qsort(nums,0,nums.length-1);
        }

        public void Qsort(int[] nums, int low, int high){
            int ind;
            if(low<high){
                ind = Partition(nums,low,high);
                Qsort(nums,low,ind-1);
                Qsort(nums,ind+1,high);
            }
        }

        //Partition的作用选取一个枢轴变量，通过交换把它放到一个位置，左边的都比它小，右边的都比它大
        /*最简单的就是枢轴选左端点，然后两端逼近.
        刚开始枢轴在左端点，先从右边找比他小的交换，交换后右边都比它大，然后从左端找比它大的交换。
        每次交换都是枢轴和一个变量交换，而且交换后外边都符合要求了，等到两边指针会和的时候，枢轴正好被交换到这个位置（也就是枢轴变量正常排序后应该出现的位置）*/
        public int Partition(int[] nums, int low,int high){
            int pivoit = nums[low];
            while(low<high){
                while(low<high && nums[high]>pivoit) high--;
                swap(nums, low, high);
                while(low<high && nums[low]<pivoit) low++;
                swap(nums, low ,high);
            }
            return low;
        }

        public void swap(int[] nums, int i, int j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
