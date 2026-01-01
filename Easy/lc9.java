// pallindrome Number
class Solution {
    public boolean isPalindrome(int x) {
        if (x<0)
            return false;
        int temp=x;
        int sum=0;
        while (temp>0){
            int r=temp%10;
            sum=sum*10+r;
            temp=temp/10;
        }
        return sum==x;
    }
    public static void main(String[] args) {
        Solution s=new Solution();
        System.out.println(s.isPalindrome(121));  // Output: true
        System.out.println(s.isPalindrome(-121)); // Output: false
        System.out.println(s.isPalindrome(10));   // Output: false
    }
}