    public static int birthdayCakeCandles(List<int> candles)
    {
        int i=0;
        int count =0;
        foreach (int candle in candles){
            
            if(candle>i) i=candle;
        }
        foreach(int candle in candles){
            if(i==candle){
                count+=1;
            }
            
        }
        return count;

    }