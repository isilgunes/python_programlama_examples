def topla_ne_varsa_git(*a):   #*a demek istediğimiz kadar parametre gönderebiliriz demektir.
    toplam = 0
    for deger in a:
        toplam += deger
    return toplam


print(topla_ne_varsa_git(3,6,87,32.7,65))

