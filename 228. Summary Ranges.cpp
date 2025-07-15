class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> result;

        if (nums.empty()) return result;

        int start = 0;

        for (int i = 1; i <= nums.size(); ++i) {
            // Check if current number is not consecutive or we've reached the end
            if (i == nums.size() || nums[i] != nums[i - 1] + 1) {
                if (start == i - 1) {
                    // Single number
                    result.push_back(to_string(nums[start]));
                } else {
                    // Range
                    result.push_back(to_string(nums[start]) + "->" + to_string(nums[i - 1]));
                }
                start = i;  // Start new range
            }
        }

        return result;
    }
};
