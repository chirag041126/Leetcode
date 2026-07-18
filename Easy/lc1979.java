class Solution {
    public int findGCD(int[] nums) {
        int max = nums[0];
        int min = nums[0];
        for (int num:nums){
            if(num>max){
                max = num;
            }
            if(num<min){
                min = num;
            }
        }
        return gcd(max,min);
    }
    public int gcd(int a , int b ){
        while(b!=0){
            int temp = b;
            b = a % b;
            a  = temp;
        }
        return a; 
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {2,5,6,9,10};
        System.out.println(sol.findGCD(nums));
    }
}