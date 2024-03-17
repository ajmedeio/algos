class Solution {
    public int pivotIndex(int[] nums) {
        int left = 0;
        int right = 0;
        for (int i = 0; i < nums.length; i++) {
            right += nums[i];
        }
        for (int pivot = 0; pivot < nums.length; pivot++) {
            right -= nums[pivot];
            if (left == right) {
                return pivot;
            }
            left += nums[pivot];
        }
        return -1;
    }
}