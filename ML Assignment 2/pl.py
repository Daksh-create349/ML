def maxSubarraySum(arr):
    currSum = arr[0]
    maxSum = arr[0]

    for i in range(1, len(arr)):
        currSum = max(arr[i], currSum + arr[i])
        maxSum = max(maxSum, currSum)

    return maxSum


arr = [2, 3, -8, 7, -1, 2, 3, -4, 5, -2,
       6, -7, 4, 8, -3, 1, -5, 9, -2, 4]

print("Maximum Subarray Sum:", maxSubarraySum(arr))