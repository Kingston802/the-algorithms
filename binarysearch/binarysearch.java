class Solution {
    public int binarySearch(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;
        int mid = 0;
        
        while(right >= left) {
            mid = left + ((right - left)/2);
            System.out.println(left);
            System.out.println(mid);
            System.out.println(right);

                
            if (mid >= nums.length) {
                break;
            }
            
            if (left == right || nums[mid] == target) {
                if (nums[mid] >= target) {
                    return mid;
                } 
                if (nums[mid] < target) {
                    return mid+1;
                }
            } 
            if (nums[mid] < target) {
                left = mid+1;
            }
            if (nums[mid] > target) {
                right = mid-1;
            }
        }
        // probably won't happen
        return mid;
    }
}
