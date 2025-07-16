    public static int diagonalDifference(List<List<int>> arr)
    {
        int primarySum = 0;
        int secondarySum = 0;
        for(int i=0;i< arr.Count;i++){
             primarySum += arr[i][i];
            secondarySum += arr[i][arr.Count - i - 1];
            
        }
        
        return Math.Abs(primarySum-secondarySum);

    }
