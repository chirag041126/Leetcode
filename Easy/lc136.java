class Solution {
    public int singleNumber(int[] nums) {
        int n=nums[0];
        for(int i = 1; i<nums.length;i++){
            n=n^nums[i];
        }
        return n;
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {2, 2, 1};
        System.out.println(sol.singleNumber(nums)); // Output: 1
    }
}