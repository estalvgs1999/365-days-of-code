/* ---------------------------------------
 *                   DAY 9
 *         Apple Interview Question
 *
 *            PRODUCT EXCEPT SELF
 *  Given an array nums of n integers where
 *  n > 1, return an array such that out[i]
 *  is equal to the product of all elements
 *  except nums[i].
 *
 *  by: @estalvgs1999
 * ---------------------------------------- */

#include <iostream>
#include <vector>
using namespace std;

vector<int> product_except_self(vector<int> nums){

    int n = nums.size();
    
    vector<int> out(n);

    out[0] = 1;

    for(int i=1; i < n; i++){
        out[i] = nums[i-1]*out[i-1];
    }

    int R = 1;
    for(int i=n-1; i>=0; i--){
        out[i] = out[i]*R;
        R = R*nums[i];
    }

    return out;
}

int main(int argc, char const *argv[])
{
    vector<int> nums = {1,2,3,4};
    vector<int> out = product_except_self(nums);

    for (vector<int>::iterator it = out.begin() ; it != out.end(); ++it)
        cout << *it<<" "; 
    cout<<endl;
    return 0;
}


