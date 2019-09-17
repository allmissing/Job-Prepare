## 基础运算
1. 不使用Math.sqrt方法实现求平方根：https://blog.csdn.net/qq_17776287/article/details/53762265  
   牛顿迭代法快速寻找平方根：假如求a的平方根的近似值，首先随便猜一个近似值x，然后不断令x等于x和a/x的平均数，迭代个六七次x的值就相当准确了。  
   其原理：求平方根等价于求方程x^2-a=0的正实根，f(x)=x^2-a的导数为f'(x)=2x，将f(x)进行一阶泰勒展开得f(x2) = f(x1)+f'(x1)(x2-x1)，将上面的式子代入得到x2 = (x1^2+a)/2*x1  

2. 大数取模定理：  
（1）（a+b)%c=(a%c+b%c)%c  
（2）（ab)%c=(a%c)(b%c)%c  

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

## 改进快排

      package Sort;

      public class ImprovedQuickSort {
          public static void main(String[] args) {
              int[] a = new int[]{2,7,8,4,6,3,9,18,43,22,5,1,88,95,37,28,90,35,17,35,44,67};
              ImprovedQuickSort qs = new ImprovedQuickSort();
              qs.QS(a);
              for(int i=0;i<a.length;i++)
                  System.out.print(a[i]+" ");
          }
          public static void QS(int[] nums){
              Qsort(nums,0,nums.length-1);
          }

          //改进4：尾递归缩减堆栈深度-》每次将low-high划分一半，处理左半边，慢慢逼近右端点
          public static void Qsort(int[] nums, int low, int high){
              int pivot;
              if(high-low>7){
                  while(low<high){
                      pivot = Partition(nums,low,high);
                      Qsort(nums,low,pivot-1);
                      low = pivot+1;
                  }
              }else InsertSort(nums,high,low);
          }

          //改进1：三数取中
          //改进2：提取出pivot，直接赋值替代交换
          public static int Partition(int[] nums, int low, int high){
              int m=(low+high)/2;
              if(nums[low]>nums[high]) swap(nums,low,high);
              if(nums[m]>nums[high]) swap(nums,m,high);
              if(nums[low]<nums[m]) swap(nums,low,m);
              int pivot = nums[low];
              while(high>low){
                  while(high>low && nums[high]>=pivot) high--;
                  nums[low] = nums[high];
                  while(high>low && nums[low]<=pivot) low++;
                  nums[high] = nums[low];
              }
              nums[low] = pivot;
              return low;
          }

          public static void swap(int[] nums, int i, int j){
              int tem = nums[i];
              nums[i] = nums[j];
              nums[j] = tem;
          }

          public static void InsertSort(int[] nums, int high, int low){
              int tem;
              for(int i=low+1;i<=high;i++){
                  if(nums[i]<nums[i-1]){
                      tem = nums[i];
                      int j;
                      for(j=i-1;nums[j]>tem && j>=low;j--) nums[j+1] = nums[j];
                      nums[j+1] = tem;
                  }
              }
          }
      }

## 归并排序（书上写法）

      public class MergingSort {
          public static void main(String[] args) {
              int[] a = new int[]{2,7,8,4,6,3,9,18,43,22,5,1,88,95,37,28,90,35,17,35,44,67};
              MergingSort ms = new MergingSort();
              ms.MS(a);
              for(int i=0;i<a.length;i++)
                  System.out.print(a[i]+" ");
          }
          public void MS(int[] a){
              this.MSorting(a,a,0,a.length-1); //这里必须是两个a
          }
          public void MSorting(int[] SR, int [] TR, int s, int t){
              int m;
              int[] TR2 = new int[SR.length];
              if(t<=s) TR[t] = SR[t];
              else{
                  m=(s+t)/2;
                  this.MSorting(SR,TR2,s,m);
                  this.MSorting(SR,TR2,m+1,t);
                  this.Merging(TR,TR2,s,m,t);
              }
          }
          public void Merging(int[] SR,int[] TR,int s,int m,int t){
              int i=s,j=m+1;
              while(m>=i && t>=j){
                  if(TR[i]>TR[j]) SR[s++] = TR[j++];
                  else SR[s++] = TR[i++];
              }
              while(m>=i) SR[s++] = TR[i++];
              while(t>=j) SR[s++] = TR[j++];
          }
      }

## 归并排序（好理解的写法）

      // 参考：https://blog.csdn.net/qq_36442947/article/details/81612870
      public class MergingSort2 {
          public static void main(String[] args) {
              int[] a = new int[]{2,7,8,4,6,3,9,18,43,22,5,1,88,95,37,28,90,35,17,35,44,67};
              MergingSort2 ms = new MergingSort2();
              ms.MSorting(a,0,a.length-1);
              for(int i=0;i<a.length;i++)
                  System.out.print(a[i]+" ");
          }

          public void MSorting(int[] SR, int s, int t){
              if(t>s){
                  int m=(s+t)/2;
                  this.MSorting(SR,s,m);
                  this.MSorting(SR,m+1,t);
                  this.Merging(SR,s,m,t);
              }
          }
          public void Merging(int[] SR,int s,int m,int t){
              int[] TR = new int[SR.length];
              for(int i=s;i<=t;i++) TR[i] = SR[i];

              int i=s,j=m+1;
              while(m>=i && t>=j){
                  if(TR[i]>TR[j]) SR[s++] = TR[j++];
                  else SR[s++] = TR[i++];
              }
              while(m>=i) SR[s++] = TR[i++];
              while(t>=j) SR[s++] = TR[j++];
          }
      }
