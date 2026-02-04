class Solution {
    public int minimumCost(int[] A) {
        int α = 51, β = 51;

        for (int i = 1; i < A.length; i++) {
            if (A[i] < α) {
                β = α;
                α = A[i];
            } else if (A[i] < β)
                β = A[i];
        }

        return A[0] + α + β;
    }
    public static void main(String args[]) {
        Solution sol = new Solution();
        int[] costs = {10, 20, 5, 30};
        System.out.println("Minimum Cost: " + sol.minimumCost(costs)); // Output: Minimum Cost: 35
    }
}