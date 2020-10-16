//Given an array nums, write a function to move all 0's to the end of it while maintaining 
//the relative order of the non-zero elements.

class Solution{
    public:
void moveZeroes( int nums[],int n)
{
    int lastNonZeroFoundAt = 0;
    for (int i = 0; i <n; i++)
    {
        if (nums[i] != 0)
        {
            nums[lastNonZeroFoundAt++] = nums[i];
        }
    }
    for (int i = lastNonZeroFoundAt; i <n ; i++)
    {
        nums[i] = 0;
    }
}
};