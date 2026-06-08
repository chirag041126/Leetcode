import java.util.*;
import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;
class Solution448 {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> number = new HashSet<>();

        for (int num : nums) {
            number.add(num);
        }

        List<Integer> result = new ArrayList<>();

        for (int i = 1; i <= nums.length; i++) {
            if (!number.contains(i)) {
                result.add(i);
            }
        }

        return result;
    }
    public static void main(String [] args){
        Solution448 s = new Solution448();
        int[] nums = {4,3,2,7,8,2,3,1};
        System.out.println(s.findDisappearedNumbers(nums));
    }
}