import java.util.HashSet;
class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> seen = new HashSet<>();
        while(n!=1){
            if(seen.contains(n)){
                return false;
            }
            seen.add(n);
            int c=0;
            while(n>0){
                int temp=n%10;
                c+=temp*temp;
                n=n/10;
            }
            n=c;
        }
        return true;
    }
    public static void main(String[] args) {
        Solution s=new Solution();
        System.out.println(s.isHappy(19));
    }
}