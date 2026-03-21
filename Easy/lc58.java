class Solution {
    public int lengthOfLastWord(String s) {
        s=s.trim();
        int count=0;
        int i=s.length()-1;
        while(i>=0 && s.charAt(i)!=' '){
            count++;
            i--;
        }
        return count;
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        String s = "Hello World";
        System.out.println(sol.lengthOfLastWord(s)); // Output: 5
    }
}