import java.util.HashMap;
import java.util.Arrays;

Class Solution{
    public int[] twoSum(int[] nums, int target){
        HashMap <Integer , Integer> map = new HashMap<>();
        for(int i = 0;i<nums.length;i++){
            int diff = target - nums[i];
            if(map.containsKey(diff)){
                return new int[]{map.get(diff),i};
            }
            map.put(nums[i],i);
        }
        return new int[]{};
    }
    public static void main(String args[]){
        Solution sol = new Solution();
        int[] nums = {2,7,11,15};
        int target = 9;
        int[] result = sol.twoSum(nums,target);
        System.out.println(Arrays.toString(result));
    }
}