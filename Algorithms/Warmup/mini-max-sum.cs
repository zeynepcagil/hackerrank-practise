public static void miniMaxSum(List<int> arr)
    {
        int n= arr.Count;
      
        int mini=arr[0];
        int maxi=arr[0];
        long sum=0;
        for(int i=0;i<n;i++){
            if(arr[i]<mini){
                mini=arr[i];
            }
            if(arr[i]>maxi){
                maxi=arr[i];
            }
            
            sum+=arr[i];
          
        }
        long miniSum=sum-maxi;
        long maxSum=sum-mini;
        
        
        Console.Write(miniSum+" "+maxSum);
    }