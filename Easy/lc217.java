class Solution {
    public boolean containsDuplicate(int[] nums){
        HashSet<Integer> set = new HashSet<>();
        for(int num : nums){
            if (set.contains(num)){
                return true;
            }
            set.add(num);
        }
        return false;
    }
    public static void main(String args[]){
        Solution sol = new Solution();
        int[] nums = {1,2,3,4,5,1};
        boolean result = sol.containsDuplicate(nums);
        System.out.println(result);
    }
}