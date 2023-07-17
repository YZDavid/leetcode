import java.util.Arrays;
import java.util.HashMap;

public class TwoSum {
    public static void main(String[] args) {
        int[] nums1 = {1,2,3};
        int[] nums2 = {2,7,11,15};
        int[] nums3 = {3,2,4};
        int[] nums4 = {3,3};
        int target1 = 5;
        int target2 = 9;
        int target3 = 6;
        int target4 = 6;
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.twoSum(nums1, target1)));
        System.out.println(Arrays.toString(solution.twoSum(nums2, target2)));
        System.out.println(Arrays.toString(solution.twoSum(nums3, target3)));
        System.out.println(Arrays.toString(solution.twoSum(nums4, target4)));
    }

    public static class Solution {
        public int[] twoSum(int[] nums, int target) {
            HashMap<Integer, Integer> hashmap = new HashMap<Integer, Integer>();
            int difference;
            for(int i=0; i<nums.length; i++) {
                difference = target - nums[i];
                if(hashmap.get(difference) != null) {
                    int[] output = {hashmap.get(difference), i};
                    return output;
                }
                hashmap.put(nums[i], i);
            }
            return null;
        }
    }

}