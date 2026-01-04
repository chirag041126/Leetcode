// Four Divisors
class Solution {
    public int sumFourDivisors(int[] nums) {
        int sum=0;
        for(int i:nums){
            int sum1=0;
            int count=2;
            for(int j=2;j<i;j++){
                if(i%j==0){
                    sum1+=j;
                    count+=1;
                    if(count==5){
                        break;
                    }
                }
            }
            if(count==4){
                sum+=(sum1+1+i);
            }
        }
        return sum;
    }
    public static void main(String[] args) {
        Solution sol=new Solution();
        int[] nums={21,4,7};
        System.out.println(sol.sumFourDivisors(nums));
    }
}
// output: 32