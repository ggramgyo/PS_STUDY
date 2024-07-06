class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> idxNums = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            
            int current = nums[i];
            int mateNum = target - current;

            if(idxNums.containsKey(mateNum)){
                Integer idxNum = idxNums.get(mateNum);
                return new int[]{idxNum, i};
            }
            idxNums.put(current, i);
        }
        return null;
    }
}
