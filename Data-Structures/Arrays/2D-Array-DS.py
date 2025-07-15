def hourglassSum(arr):
  
    max_hourglass_sum = float('-inf') 
    for i in range(4):
        for j in range(4):
            current_sum= arr[i][j+2]+arr[i][j+1]+arr[i][j]
            current_sum+=arr[i+1][j+1]
            current_sum+=arr[i+2][j+2]+arr[i+2][j+1]+arr[i+2][j]
            if current_sum > max_hourglass_sum:
                 max_hourglass_sum = current_sum
                
    return max_hourglass_sum