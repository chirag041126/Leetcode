class Solution {
    public int gcdOfOddEvenSums(int n) {
        int sumodd = n*n;
        int sumeven = n*(n+1);
        return gcd(sumodd,sumeven);
    }
    private int gcd(int x, int y){
        return y == 0 ? x : gcd(y,x % y) ;
    }
    public static void main(String args[]) {
        Solution sol = new Solution();
        int n = 5;
        System.out.println(sol.gcdOfOddEvenSums(n));
}