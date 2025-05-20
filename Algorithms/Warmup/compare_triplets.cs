   public static List<int> compareTriplets(List<int> a, List<int> b)
    {
        int a_point=0;
        int b_point=0;
        for(int i=0; i< a.Count;i++){
            if(a[i]>b[i]){
                a_point++;
            }

            else if(a[i]<b[i]){
              b_point++;  
            } 
               
        }
        List<int> rList = new List<int>{a_point,b_point};
           
        
        return rList; 
    }

