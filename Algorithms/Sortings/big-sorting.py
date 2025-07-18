def bigSorting(unsorted):
    # sorted() fonksiyonu ile 'unsorted' listesini sıralıyoruz.
    # key parametresi ile sıralamanın nasıl yapılacağını belirtiyoruz.
    # lambda x: (len(x), x) ifadesi her bir öğeyi önce uzunluğuna göre,
    # sonra uzunluklar eşitse kendi string değerine göre sıralamak için kullanılır.
    # Böylece sayılar string olarak saklansa bile önce basamak sayısına,
    # sonra alfabetik (sayısal sıralama gibi) olarak sıralanır.
    return sorted(unsorted, key=lambda x: (len(x), x))