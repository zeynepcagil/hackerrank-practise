    public static string timeConversion(string s)
    {
            string meridiem = s.Substring(s.Length - 2); // "AM" veya "PM"
    string[] parts = s.Substring(0, 8).Split(':');    // ["12", "01", "00"]

    int hour = int.Parse(parts[0]);
    string minute = parts[1];
    string second = parts[2];

    if (meridiem == "AM")
    {
        if (hour == 12)
            hour = 0;
    }
    else if (meridiem == "PM")
    {
        if (hour != 12)
            hour += 12;
    }

    return $"{hour:D2}:{minute}:{second}";


    }

