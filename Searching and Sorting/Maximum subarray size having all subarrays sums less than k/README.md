<b>Maximum subarray size having all subarrays sums less than k</b>

Given an array of positive integers arr[] of size n, and an integer k. The task is to find the maximum subarray size such that all subarrays of that size have sum less than or equals to k.

Examples : 

Input :  arr[] = [1, 2, 3, 4], k = 8.

Output : 2

Explanation: Following are the sum of subarray of size 1 to 4.

Sum of subarrays of size 1: 1, 2, 3, 4. 

Sum of subarrays of size 2: 3, 5, 7. 

Sum of subarrays of size 3: 6, 9. 

Sum of subarrays of size 4: 10. 

So, maximum subarray size such that all subarrays of that size have the sum of elements less than 8 is 2.

Input:  arr[] = [1, 2, 10, 4], k = 8. 

Output : -1 

Explanation: There is an array element (10) with value greater than k, so subarray sum cannot be less than k. 

Input :  arr[] = [1, 2, 10, 4], k = 14 

Output : 2
