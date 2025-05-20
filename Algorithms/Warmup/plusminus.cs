    public static void plusMinus(List<int> arr)
    {
        int positive_numb=0;
        int negative_numb=0;
        int zero_numb=0;
        for(int i=0;i<arr.Count;i++){
            if(arr[i]<0){
                negative_numb++;
            }
            else if(arr[i]>0){
                positive_numb++;
            }
            else zero_numb++;
            
            
        }
        float result=(float)positive_numb/arr.Count;
        float result2=(float)negative_numb/arr.Count;
        float result3=(float)zero_numb/arr.Count;
        Console.WriteLine(result.ToString("F6"));
        Console.WriteLine(result2.ToString("F6"));
        Console.WriteLine(result3.ToString("F6"));

    }

}