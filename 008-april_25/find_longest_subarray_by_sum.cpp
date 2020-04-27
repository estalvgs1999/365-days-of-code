/* ---------------------------------------
 *                  DAY 8 
 *       Facebook Interview Question 
 *
 *      FIND LONGEST SUBARRAY BY SUM 
 *  
 * Given an array of integers and a value 
 *  of sum s, return the longest subarray 
 *  whose elements add up to s.
 *
 *  Input:
 *  s : sum; 0 < s < 10⁹
 *  arr: int array
 *         |_ 1 < arr.length < 10⁵
 *         |_ 0 < arr[i] < 10⁴
 * 
 *  Output:
 *  An array that contains two elements that
 *  represents the left and right bounds of
 *  the subarray respectively (1-based).
 *  If there no subarray, return [-1] 
 *
 *  by: @estalvgs1999 
 * ---------------------------------------*/

#include <iostream>
#include <vector>

using namespace std;

// Solution #1
// Complexity => O(n)
vector<int> findLongestSubarrayBySum(int s, vector<int> arr){

    int currentSum = 0;
    int left = 0, right = 0;
    vector<int> result(2);

    result.push_back(-1);

    while(right < arr.size()){

        currentSum += arr[right];

        while(left < right && currentSum > s)
            currentSum -= arr[left++];
        
        if(currentSum == s && (result.size() == -1 || result[1]-result[0] < right-left)){
            result[0] = left+1, result[1] = right+1;
        }

        right++;
    }
    
    return result; 
}

int main(int argc, char const *argv[])
{
    vector<int> arr = {1,2,3,7,5},result;
    result = findLongestSubarrayBySum(5,arr);
    
    cout<<"Output: [ "<<result[0]<<" , "<<result[1]<<"]"<<endl;
    
    return 0;
}

